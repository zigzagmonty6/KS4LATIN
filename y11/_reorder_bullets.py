"""Reorder explanation bullets into English reading order (SVO).

Rule — WITHIN each clause (bounded by conjunction bullets et / sed / nam / -que):
  1. Subject (bullet containing 'subject' or 'emphatic subject')
  2. Adjective agreeing with subject (bullet referencing 'agreeing with <subject-word>')
  3. Verb (bullet tagged '— verb,' OR '— PPP')
  4. Direct object (accusative or second-accusative)
  5. Adjective agreeing with object
  6. Dative ('DATIVE singular' or 'DATIVE plural')
  7. Prepositional phrases
  8. Adverbs, negations
Conjunction bullets (et/sed/nam/-que) act as dividers and stay in place.
"""

import re, pathlib

PATH = pathlib.Path(r"C:\Users\mmhun\Desktop\y11_latin_gcse\y11\data.py")

SRC = PATH.read_text(encoding="utf-8")

# A bullet is the chunk starting with "• " and ending before the next "• " or end-of-string.
CONJ_WORDS = {"et", "sed", "nam", "-que", "but", "and", "for"}

def bullet_rank(bullet, subj_words, obj_words):
    """Lower = earlier. Conjunctions return None (treated as separator).

    English reading order inside one clause:
      0 subject
      0.5 demonstrative / subject-modifier pronoun
      1 adjective or PPP agreeing with subject
      2 verb (including auxiliary)
      3 direct object
      4 adjective or PPP agreeing with object
      5 dative
      6 prepositional phrase
      7 negation
      8 adverb
    """
    b = bullet.lower()
    m = re.match(r'\s*•\s*([^\s(]+)', bullet)
    head = m.group(1).lower() if m else ""
    if head in CONJ_WORDS:
        return None  # divider
    if "subject" in b:
        return 0
    # "agreeing with <word>" disambiguation
    agreeing_with = None
    am = re.search(r'agreeing with\s+([a-z]+)', b)
    if am:
        agreeing_with = am.group(1)
    if "— verb," in bullet or "auxiliary" in b:
        return 2
    if "— ppp" in b:
        if agreeing_with and agreeing_with in (w.lower() for w in subj_words):
            return 1
        if agreeing_with and agreeing_with in (w.lower() for w in obj_words):
            return 4
        return 4  # default: assume modifying object
    if "adjective" in b and "agreeing with" in b:
        if agreeing_with and agreeing_with in (w.lower() for w in subj_words):
            return 1
        if agreeing_with and agreeing_with in (w.lower() for w in obj_words):
            return 4
        return 1  # default: assume modifying subject
    if "direct object" in b:
        return 3
    if "dative" in b:
        return 5
    if "prepositional phrase" in b:
        return 6
    if "negates" in b:
        return 7
    if "adverb" in b:
        return 8
    if "conjunction" in b:
        return None
    if "demonstrative" in b or ("pronoun" in b and "accusative" not in b and "dative" not in b):
        return 0.5
    return 9

def subject_words(clause_bullets):
    """Extract the Latin head word of any bullet marked 'subject'."""
    out = []
    for bl in clause_bullets:
        if "subject" in bl.lower():
            m = re.match(r'\s*•\s*([^\s(]+)', bl)
            if m: out.append(m.group(1))
    return out

def object_words(clause_bullets):
    """Extract the Latin head word of any bullet marked 'direct object'."""
    out = []
    for bl in clause_bullets:
        if "direct object" in bl.lower():
            m = re.match(r'\s*•\s*([^\s(]+)', bl)
            if m: out.append(m.group(1))
    return out

def reorder_explanation(expl):
    # Split into bullets preserving the leading "• "
    # Bullets are separated by newlines in the source.
    bullets = [b for b in re.split(r'\n(?=•)', expl.strip()) if b.strip()]
    if len(bullets) <= 2:
        return expl  # nothing to reorder
    # Split into clauses at conjunction bullets.
    clauses = []  # list of (pre_conj_bullets, conj_bullet_or_None)
    current = []
    for b in bullets:
        m = re.match(r'\s*•\s*([^\s(]+)', b)
        head = m.group(1).lower() if m else ""
        if head in CONJ_WORDS:
            clauses.append((current, b))
            current = []
        else:
            current.append(b)
    clauses.append((current, None))

    new_bullets = []
    for idx, (clause, conj) in enumerate(clauses):
        subj = subject_words(clause)
        obj = object_words(clause)
        keyed = [((bullet_rank(b, subj, obj) if bullet_rank(b, subj, obj) is not None else 99), i, b)
                 for i, b in enumerate(clause)]
        keyed.sort(key=lambda x: (x[0], x[1]))
        new_bullets.extend(b for _, _, b in keyed)
        if conj is not None:
            new_bullets.append(conj)

    return "\n".join(new_bullets)


# Find every explanation string (triple-quoted not used; these are parenthesised
# string literals joined with \n). Match "explanation": ( ... ),
pat = re.compile(
    r'("explanation":\s*\(\s*)("(?:[^"\\]|\\.)*"(?:\s*\n\s*"(?:[^"\\]|\\.)*")*)(\s*\),)',
    re.DOTALL,
)

def rewrite(m):
    prefix, literal_block, suffix = m.group(1), m.group(2), m.group(3)
    # Reconstruct the actual string content from the python-literal pieces
    # Each piece is a "..." literal; their concatenation is the explanation text.
    pieces = re.findall(r'"((?:[^"\\]|\\.)*)"', literal_block)
    raw = "".join(p.replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\") for p in pieces)
    reordered = reorder_explanation(raw)
    if reordered == raw:
        return m.group(0)
    # Re-emit as multi-line literal, one bullet per "• ..." line
    lines = reordered.split("\n")
    # Escape for python literal
    out_lines = []
    for i, line in enumerate(lines):
        esc = line.replace("\\", "\\\\").replace('"', '\\"')
        if i < len(lines) - 1:
            out_lines.append(f'"{esc}\\n"')
        else:
            out_lines.append(f'"{esc}"')
    # Use the same indent as original (approximate: 12 spaces from the captured context)
    joined = ("\n" + " " * 12).join(out_lines)
    return f'{prefix}{joined}{suffix}'

# Only process Node 1 range: lines ~355..1300 (SENTENCES_PRESENT_TEST through SENTENCES_REVIEW end)
start = SRC.find("SENTENCES_PRESENT_TEST")
# End at the line after SENTENCES_REVIEW closes — find the next top-level assignment after it
rev_pos = SRC.find("SENTENCES_REVIEW = [")
# Find the matching bracket-close: naive — find the next "\n]\n" after rev_pos
end = SRC.find("\n]\n", rev_pos) + len("\n]\n")
if start < 0 or end <= start:
    raise SystemExit("Could not locate Node 1 range in data.py")

before, middle, after = SRC[:start], SRC[start:end], SRC[end:]
matches = list(pat.finditer(middle))
print(f"Found {len(matches)} explanation blocks")
if matches:
    print("First match literal block:")
    print(matches[0].group(2)[:300])
    print("---")
    pieces = re.findall(r'"((?:[^"\\]|\\.)*)"', matches[0].group(2))
    raw = "".join(p.replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\") for p in pieces)
    # (debug prints suppressed — console encoding issues)
    pass

changes = [0]
def rewrite_count(m):
    out = rewrite(m)
    if out != m.group(0):
        changes[0] += 1
    return out

new_middle = pat.sub(rewrite_count, middle)
PATH.write_text(before + new_middle + after, encoding="utf-8")
print(f"Rewrote {changes[0]} explanation blocks in Node 1 range")
