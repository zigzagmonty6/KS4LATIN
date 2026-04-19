"""
Latin GCSE Mastery Platform — FastAPI Backend
"""
import json, random, re
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from data import SETS, SETS_BY_ID, STUDENTS, VERBS_1ST_TOP150
from database import init_db, get_db
from marking import (
    check_vocab, check_latin_typed, check_gap_fill,
    check_all_four_parts, check_sentence, check_parsing
)

app = FastAPI()
init_db()

# ── Helpers ───────────────────────────────────────────────────────────────────

def verb_dict(v):
    """Convert VERBS_1ST_TOP150 tuple to a dict for the frontend."""
    return {
        "present":v[0], "infinitive":v[1], "perfect":v[2],
        "ppp":v[3],  # None for festino/navigo/appropinquo
        "eng_present":re.sub(r'\bi\b', 'I', v[4]), "eng_infinitive":v[5],
        "eng_perfect":re.sub(r'\bi\b', 'I', v[6]), "eng_ppp":v[7],
    }

def set_detail(s, pupil_id=None):
    """Build the full set detail dict returned from /api/sets/{id}."""
    r = {
        "id": s["id"],
        "node": s["node"],
        "node_title": s["node_title"],
        "title": s["title"],
        "type": s["type"],
        "optional": s.get("optional", False),
        "sell": s.get("sell", ""),
        "footnote": s.get("footnote", ""),
        "pass_mark": s.get("pass_mark"),
        "badge": s.get("badge"),  # e.g. "Principal Part"
    }
    if "screens" in s:
        r["screens"] = s["screens"]
        
    content = s.get("content", {})
    if s["type"] in ("vocab", "verbs"):
        mode = content.get("mode","meanings")
        r["mode"] = mode
        if "verbs" in content:
            r["verbs"] = [verb_dict(v) for v in content["verbs"]]
        if "vocab" in content:
            r["vocab"] = content["vocab"]

    elif s["type"] == "building_parts":
        r["verbs"] = [verb_dict(v) for v in content["verbs"]]
        r["mode"] = content["mode"]
        r["show_parts_so_far"] = content.get("show_parts_so_far", 1)
        r["pattern_screen"] = content.get("pattern_screen")
        r["gap_positions"] = content.get("gap_positions")

    elif s["type"] == "tense_id":
        qs = list(content["questions"])
        random.shuffle(qs)
        r["questions"] = qs
        r["tense_options"] = ["present","imperfect","future","perfect","pluperfect"]

    elif s["type"] == "parsing":
        qs = list(content["questions"])
        random.shuffle(qs)
        r["questions"] = qs

    elif s["type"] == "parsing_mcq":
        qs = list(content["questions"])
        random.shuffle(qs)
        r["questions"] = qs

    elif s["type"] == "translate_form":
        qs = list(content["questions"])
        random.shuffle(qs)
        r["questions"] = qs

    elif s["type"] == "sentences":
        sentences = list(content["sentences"])
        for i, sent in enumerate(sentences):
            sent["original_index"] = i
        r["sentences"] = sentences

    elif s["type"] == "review":
        sentences = list(content.get("sentences", []))
        for i, sent in enumerate(sentences):
            sent["original_index"] = i
        r["sentences"] = sentences
        r["parse_translate"] = list(content.get("parse_translate", []))
        random.shuffle(r["parse_translate"])

    elif s["type"] == "concept":
        # Concept sets have questions (e.g. VERB_IDENTIFY) - pass through as questions
        if "questions" in content:
            qs = list(content["questions"])
            r["questions"] = qs

    elif s["type"] == "reference":
        pass  # sell text is sufficient

    return r

# ── Static files & root ───────────────────────────────────────────────────────

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

# ── Pupils ────────────────────────────────────────────────────────────────────

@app.get("/api/pupils")
def get_pupils():
    with get_db() as db:
        rows = db.execute("SELECT id, first_name FROM pupils ORDER BY first_name").fetchall()
        return [{"id": r["id"], "first_name": r["first_name"]} for r in rows]

# ── Login ─────────────────────────────────────────────────────────────────────

class LoginReq(BaseModel):
    first_name: str

@app.post("/api/login")
def login(req: LoginReq):
    with get_db() as db:
        row = db.execute("SELECT id, first_name FROM pupils WHERE first_name=?",
                         (req.first_name,)).fetchone()
        if not row:
            raise HTTPException(404, "Pupil not found")
        pupil = {"id": row["id"], "first_name": row["first_name"]}
        progress = db.execute(
            "SELECT set_id, status, best_score FROM pupil_progress WHERE pupil_id=?",
            (row["id"],)).fetchall()
        prog_list = [{"set_id": r["set_id"], "status": r["status"], "best_score": r["best_score"]}
                     for r in progress]
        return {"pupil": pupil, "progress": prog_list}

# ── Teacher auth ──────────────────────────────────────────────────────────────

class TeacherAuthReq(BaseModel):
    password: str

@app.post("/api/teacher/auth")
def teacher_auth(req: TeacherAuthReq):
    if req.password == "latinmagister":
        return {"success": True}
    raise HTTPException(403, "Wrong password")

# ── Sets ──────────────────────────────────────────────────────────────────────

@app.get("/api/sets")
def get_sets():
    return [{"id":s["id"],"title":s["title"],"type":s["type"],
             "node":s["node"],"node_title":s["node_title"],
             "optional":s.get("optional",False),"pass_mark":s.get("pass_mark"),
             "badge":s.get("badge")}
            for s in SETS]

@app.get("/api/sets/{set_id}")
def get_set(set_id: int):
    s = SETS_BY_ID.get(set_id)
    if not s:
        raise HTTPException(404, "Set not found")
    return set_detail(s)

# ── Progress ──────────────────────────────────────────────────────────────────

@app.get("/api/pupil/{pupil_id}/progress")
def get_progress(pupil_id: int):
    with get_db() as db:
        rows = db.execute(
            "SELECT set_id, status, best_score FROM pupil_progress WHERE pupil_id=?",
            (pupil_id,)).fetchall()
        return [{"set_id": r["set_id"], "status": r["status"], "best_score": r["best_score"]}
                for r in rows]

# ── Check ─────────────────────────────────────────────────────────────────────

class CheckReq(BaseModel):
    pupil_id: int
    set_id: int
    question_type: str
    question_text: str
    pupil_answer: str
    correct_answer: Optional[str] = ""
    sentence_index: Optional[int] = None
    time_taken_ms: Optional[int] = 0
    # For parsing (full)
    tense: Optional[str] = None
    person: Optional[str] = None
    number: Optional[str] = None

@app.post("/api/check")
def check(req: CheckReq):
    s = SETS_BY_ID.get(req.set_id)
    qt = req.question_type

    # ── Vocab (English meanings) ──────────────────────────────────────────────
    if qt in ("vocab", "typed"):
        # Find the vocab item by id or latin field
        vocab_item = None
        if s and s["type"] in ("vocab", "verbs"):
            content = s.get("content", {})
            if "verbs" in content:
                for v in content["verbs"]:
                    if v[0] == req.question_text or v[1] == req.question_text:
                        vocab_item = {"english": [v[4]], "pos": "verb"}
                        break
            elif "vocab" in content:
                # First try matching by id (handles in_acc vs in_abl ambiguity)
                for item in content["vocab"]:
                    if item.get("id") == req.question_text:
                        vocab_item = item
                        break
                # Fallback: match by latin field
                if not vocab_item:
                    for item in content["vocab"]:
                        if item["latin"] == req.question_text:
                            vocab_item = item
                            break
        if not vocab_item:
            # Fallback: parse correct_answer, split by comma only (preserves he/she forms)
            parts = [p.strip() for p in (req.correct_answer or "").split(",") if p.strip()]
            vocab_item = {"english": parts, "pos": ""}
        res = check_vocab(req.pupil_answer, vocab_item)

    # ── Flashcard rating (just log, always correct) ───────────────────────────
    elif qt == "flashcard_rating":
        res = {"result": req.pupil_answer, "counts_as_correct": req.pupil_answer == "got_it",
               "message": ""}

    # ── Multiple choice ───────────────────────────────────────────────────────
    elif qt in ("mc", "parsing_mcq"):
        correct = req.correct_answer
        is_right = req.pupil_answer == correct
        res = {"result": "correct" if is_right else "wrong",
               "counts_as_correct": is_right,
               "message": "Correct!" if is_right else f"The answer is: **{correct}**",
               "correct_answer": correct}

    # ── Tense ID ──────────────────────────────────────────────────────────────
    elif qt == "tense_id":
        correct = req.correct_answer
        is_right = req.pupil_answer == correct
        res = {"result": "correct" if is_right else "wrong",
               "counts_as_correct": is_right,
               "message": "Correct!" if is_right else f"The answer is: **{correct}**",
               "correct_answer": correct}

    # ── Full parsing (person + number + tense) ────────────────────────────────
    elif qt == "parsing":
        parts = (req.correct_answer or "").split("|")
        if len(parts) == 3:
            correct_tense, correct_person, correct_number = parts
            res = check_parsing(
                req.tense or "", req.person or "", req.number or "",
                correct_tense, correct_person, correct_number
            )
        else:
            res = {"result":"wrong","message":"Answer data error.","counts_as_correct":False}

    # ── Latin typed (single principal part) ───────────────────────────────────
    elif qt == "latin_typed":
        res = check_latin_typed(req.pupil_answer, req.correct_answer)

    elif qt == "all_four_typed":
        parts = (req.correct_answer or "").split()
        if len(parts) == 3:
            res = check_all_four_parts(req.pupil_answer, parts[0], parts[1], parts[2])
        elif len(parts) == 2:
            # Verbs with no PPP — only inf and perf required
            from marking import norm_latin, split_parts
            raw_parts = split_parts(req.pupil_answer)
            if len(raw_parts) != 2:
                res = {"result":"wrong","counts_as_correct":False,
                       "message":f"Type two parts: infinitive and perfect. The answer is: *{parts[0]} {parts[1]}*",
                       "correct_answer":f"{parts[0]} {parts[1]}"}
            else:
                ok_inf  = norm_latin(raw_parts[0]) == norm_latin(parts[0])
                ok_perf = norm_latin(raw_parts[1]) == norm_latin(parts[1])
                if ok_inf and ok_perf:
                    res = {"result":"correct","message":"Correct!",
                           "correct_answer":f"{parts[0]} {parts[1]}","counts_as_correct":True}
                else:
                    errors = []
                    if not ok_inf:  errors.append(f"infinitive: *{parts[0]}*")
                    if not ok_perf: errors.append(f"perfect: *{parts[1]}*")
                    res = {"result":"wrong","counts_as_correct":False,
                           "message":"Check: " + "; ".join(errors) + f". Answer: *{parts[0]} {parts[1]}*",
                           "correct_answer":f"{parts[0]} {parts[1]}"}
        else:
            res = {"result":"wrong","message":"Answer data error.","counts_as_correct":False}

    # ── Sentence ──────────────────────────────────────────────────────────────
    elif qt == "sentence":
        sentence_obj = None
        if s and s["type"] in ("sentences", "review"):
            sents = s["content"]["sentences"]
            idx = req.sentence_index
            if idx is not None and 0 <= idx < len(sents):
                sentence_obj = sents[idx]
        if not sentence_obj:
            # Fallback: build minimal sentence object from question_text
            sentence_obj = {"latin": req.question_text,
                            "english": [req.correct_answer] if req.correct_answer else [""],
                            "explanation": ""}
        res = check_sentence(req.pupil_answer, sentence_obj)

    elif qt == "translate_form":
        correct = req.correct_answer
        # Build a minimal vocab-like object so we get the 'you sg/pl' warning and typo detection
        import re as _re
        # check_sentence handles the 'you (sg/pl)' warning and tense checks
        sentence_obj = {
            "latin": req.question_text,
            "english": [correct],
            "explanation": ""
        }
        res = check_sentence(req.pupil_answer, sentence_obj)

    # ── Parse and Translate (review set) ─────────────────────────────────────
    elif qt == "parse_translate":
        # correct_answer format: "tense|person|number|translation"
        parts_ca = (req.correct_answer or "").split("|")
        if len(parts_ca) == 4:
            correct_tense, correct_person, correct_number, correct_translation = parts_ca
            # Check parsing part
            parse_res = check_parsing(
                req.tense or "", req.person or "", req.number or "",
                correct_tense, correct_person, correct_number
            )
            # Build a minimal sentence object for translation check.
            # If the correct translation contains a sg/pl marker (e.g. "you (sg) will kill"),
            # also accept the bare version ("you will kill") since the pupil already
            # specified sg/pl in the parse dropdowns.
            import re as _re
            bare_trans = _re.sub(r'\s*\(sg\)|\s*\(pl\)', '', correct_translation).strip()
            translation_variants = [correct_translation]
            if bare_trans != correct_translation:
                translation_variants.append(bare_trans)
            sentence_obj = {
                "latin": req.question_text,
                "english": translation_variants,
                "explanation": f"The answer is: **{correct_translation}**"
            }
            trans_res = check_sentence(req.pupil_answer, sentence_obj)
            parse_ok = parse_res["counts_as_correct"]
            trans_ok = trans_res["counts_as_correct"]
            if parse_ok and trans_ok:
                res = {"result": "correct", "message": "Correct!", "counts_as_correct": True,
                       "correct_answer": correct_translation}
            else:
                msgs = []
                if not parse_ok:
                    msgs.append(parse_res["message"])
                if not trans_ok:
                    msgs.append(f"Translation: {trans_res['message']}")
                res = {"result": "wrong",
                       "message": " | ".join(msgs),
                       "counts_as_correct": False,
                       "correct_answer": correct_translation,
                       "parse_correct": parse_ok,
                       "trans_correct": trans_ok}
        else:
            res = {"result": "wrong", "message": "Answer data error.", "counts_as_correct": False}

    else:
        res = {"result":"wrong","message":f"Unknown question type: {qt}",
               "counts_as_correct":False,"correct_answer":""}

    # ── Log to DB ─────────────────────────────────────────────────────────────
    if req.pupil_id > 0:
        with get_db() as db:
            db.execute(
                """INSERT INTO attempt_log
                   (pupil_id, set_id, question_type, question_text,
                    pupil_answer, correct_answer, result, time_taken_ms)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (req.pupil_id, req.set_id, qt, req.question_text,
                 req.pupil_answer, req.correct_answer,
                 res.get("result",""), req.time_taken_ms or 0)
            )

    return res

# ── Complete (save score, unlock next set) ────────────────────────────────────

class CompleteReq(BaseModel):
    pupil_id: int
    set_id: int
    score: float

@app.post("/api/complete")
def complete(req: CompleteReq):
    s = SETS_BY_ID.get(req.set_id)
    if not s:
        raise HTTPException(404, "Set not found")

    passed = req.score >= (s.get("pass_mark") or 80)

    with get_db() as db:
        # Update this set's progress
        existing = db.execute(
            "SELECT best_score FROM pupil_progress WHERE pupil_id=? AND set_id=?",
            (req.pupil_id, req.set_id)).fetchone()
        new_best = max(req.score, existing["best_score"] if existing else 0)
        new_status = "passed" if passed else "available"
        db.execute(
            """INSERT INTO pupil_progress (pupil_id, set_id, status, best_score)
               VALUES (?,?,?,?)
               ON CONFLICT(pupil_id,set_id) DO UPDATE SET
               status=excluded.status, best_score=excluded.best_score""",
            (req.pupil_id, req.set_id, new_status, new_best)
        )

        if passed:
            _unlock_next(db, req.pupil_id, req.set_id)

    return {"success": True, "passed": passed, "best_score": new_best}

def _unlock_set(db, pupil_id, set_id):
    """Mark a single set as available if currently locked."""
    db.execute(
        """INSERT INTO pupil_progress (pupil_id, set_id, status, best_score)
           VALUES (?,?,'available',0)
           ON CONFLICT(pupil_id,set_id) DO UPDATE SET
           status=CASE WHEN status='locked' THEN 'available' ELSE status END""",
        (pupil_id, set_id)
    )

def _unlock_node_start(db, pupil_id, node_num):
    """Unlock the first non-optional set of node_num, plus any optional sets before it."""
    node_sets = [x for x in SETS if x["node"] == node_num]
    if not node_sets:
        return
    # Unlock all optional sets that appear before the first non-optional
    for x in node_sets:
        if x.get("optional"):
            _unlock_set(db, pupil_id, x["id"])
        else:
            # First non-optional — unlock it and stop
            _unlock_set(db, pupil_id, x["id"])
            break

def _unlock_next(db, pupil_id, completed_set_id):
    """Unlock the next appropriate sets after passing."""
    s = SETS_BY_ID.get(completed_set_id)
    if not s: return

    # Reference sets (node 0) — unlock all other intro sets + first set of node 1
    if s["type"] == "reference" and s["node"] == 0:
        # Ensure all other node 0 sets are available too
        for x in SETS:
            if x["node"] == 0:
                _unlock_set(db, pupil_id, x["id"])
        _unlock_node_start(db, pupil_id, 1)
        return

    current_node = s["node"]
    all_node = [x for x in SETS if x["node"] == current_node]
    current_pos = next((i for i,x in enumerate(all_node) if x["id"]==completed_set_id), -1)

    # Find the next non-optional set in the same node
    same_node_non_opt = [x for x in all_node if not x.get("optional")]
    ids = [x["id"] for x in same_node_non_opt]

    try:
        idx = ids.index(completed_set_id)
        is_optional = False
    except ValueError:
        idx = -1
        is_optional = True

    if not is_optional and idx + 1 < len(ids):
        # There is a next non-optional set in this node — unlock it
        _unlock_set(db, pupil_id, ids[idx + 1])
        # Also unlock any optional sets between this and the next non-optional
        for x in all_node[current_pos+1:]:
            if not x.get("optional"):
                break
            _unlock_set(db, pupil_id, x["id"])

    elif not is_optional and idx + 1 >= len(ids):
        # This was the LAST non-optional set in the node — unlock the next node
        node_nums = sorted(set(x["node"] for x in SETS))
        try:
            node_idx = node_nums.index(current_node)
        except ValueError:
            return
        if node_idx + 1 < len(node_nums):
            next_node = node_nums[node_idx + 1]
            _unlock_node_start(db, pupil_id, next_node)

    # Optional set completed — also unlock the next non-optional in same node
    if is_optional and current_pos >= 0:
        for x in all_node[current_pos+1:]:
            if not x.get("optional"):
                _unlock_set(db, pupil_id, x["id"])
                break

@app.get("/api/teacher/progress")
def teacher_progress():
    with get_db() as db:
        rows = db.execute("""
            SELECT p.first_name, pp.set_id, pp.status, pp.best_score
            FROM pupils p
            JOIN pupil_progress pp ON pp.pupil_id = p.id
            ORDER BY p.first_name, pp.set_id
        """).fetchall()
        result = {}
        for r in rows:
            name = r["first_name"]
            if name not in result:
                result[name] = []
            result[name].append({
                "set_id": r["set_id"],
                "status": r["status"],
                "best_score": r["best_score"]
            })
        return result

# ── Session stubs (frontend expects these) ────────────────────────────────────

class SessionStartReq(BaseModel):
    pupil_id: int
    set_id: int

@app.post("/api/session/start")
def session_start(req: SessionStartReq):
    return {"session_id": 0}

@app.post("/api/session/end")
def session_end():
    return {"success": True}

# ── Teacher dashboard endpoints ───────────────────────────────────────────────

@app.get("/api/teacher/overview")
def teacher_overview():
    with get_db() as db:
        pupils = db.execute("SELECT id, first_name FROM pupils ORDER BY first_name").fetchall()
        result = []
        for p in pupils:
            rows = db.execute(
                "SELECT set_id, status, best_score FROM pupil_progress WHERE pupil_id=? ORDER BY set_id",
                (p["id"],)).fetchall()
            sets_done = sum(1 for r in rows if r["status"] == "passed")
            avg = sum(r["best_score"] for r in rows if r["status"] == "passed") / max(sets_done, 1)
            result.append({
                "pupil_id": p["id"],
                "name": p["first_name"],
                "sets_passed": sets_done,
                "avg_score": round(avg, 1),
                "progress": [{"set_id": r["set_id"], "status": r["status"], "best_score": r["best_score"]} for r in rows]
            })
        return result

@app.get("/api/teacher/weak-verbs")
def teacher_weak_verbs():
    with get_db() as db:
        rows = db.execute("""
            SELECT question_text, COUNT(*) as attempts,
                   SUM(CASE WHEN result='wrong' THEN 1 ELSE 0 END) as wrong_count
            FROM attempt_log
            WHERE question_type IN ('latin_typed','gap_fill','all_four_typed')
            GROUP BY question_text
            HAVING attempts > 2
            ORDER BY (CAST(wrong_count AS REAL)/attempts) DESC
            LIMIT 20
        """).fetchall()
        return [{"form": r["question_text"], "attempts": r["attempts"],
                 "error_rate": round(r["wrong_count"]/r["attempts"]*100)} for r in rows]

@app.get("/api/teacher/misconceptions")
def teacher_misconceptions():
    with get_db() as db:
        rows = db.execute("""
            SELECT question_text, pupil_answer, correct_answer, COUNT(*) as n
            FROM attempt_log
            WHERE result = 'wrong' AND pupil_answer != '' AND pupil_answer != 'TIMEOUT'
            GROUP BY question_text, pupil_answer
            HAVING n > 1
            ORDER BY n DESC
            LIMIT 30
        """).fetchall()
        return [{"question": r["question_text"], "wrong_answer": r["pupil_answer"],
                 "correct": r["correct_answer"], "count": r["n"]} for r in rows]
