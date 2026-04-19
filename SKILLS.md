# Latin GCSE Platform — Content & Authoring Standards
## Based on the Perfected Node 1 (1st Conjugation)

---

## 1. CANONICAL 16-SET NODE STRUCTURE

Every conjugation node follows this exact sequence. Set numbering and `_order` must reflect this:

| Pos | Title | type | badge | notes |
|-----|-------|------|-------|-------|
| 1 | Sentence Vocabulary | `vocab` | — | optional:True |
| 2 | Present: 'I' Form | `verbs` | Principal Part | grammar screen required |
| 3 | Present Tense Endings | `translate_form` | — | table screen required |
| 4 | The Present Tense | `sentences` | — | 10 sentences |
| 5 | Infinitive | `building_parts` | Principal Part | pattern_screen required |
| 6 | The Imperfect Tense | `translate_form` | — | table screen required |
| 7 | The Future Tense | `translate_form` | — | table screen required |
| 8 | The Present System | `sentences` | — | 10 sentences, all 3 present-system tenses |
| 9 | Perfect: 'I' Form | `building_parts` | Principal Part | pattern_screen required |
| 10 | Perfect Tense: All Endings | `translate_form` | — | table screen required |
| 11 | The Pluperfect Tense | `translate_form` | — | table screen required |
| 12 | Perfect & Pluperfect | `sentences` | — | 10 sentences |
| 13 | Perfect Passive Participle (PPP) | `building_parts` | Principal Part | pattern_screen required |
| 14 | Perfect Passive Participles | `sentences` | — | 10 sentences |
| 15 | Build the Principal Parts | `building_parts` | — | all four, gap_positions:[1,2,3] |
| 16 | Review | `review` | test | sentences + parse_translate |

`_order` within a node: vocab → pp1_verbs → present_endings → present_sentences → infinitive → imperfect → future → present_system_sentences → perfect_pp3 → perfect_endings → pluperfect → perf_pluperf_sentences → ppp_pp4 → ppp_sentences → all_parts → review

---

## 2. PYTHON DATA STRUCTURE — FIELD SPECIFICATIONS

### 2a. Set-level fields (every set)
```python
{
    "id": <int>,
    "node": <int>,
    "node_title": "<string>",
    "title": "<string>",
    "type": "<verb|vocab|translate_form|sentences|building_parts|review|...>",
    "badge": "<string>",        # only when applicable: "Principal Part" or "test"
    "optional": True,           # only on vocab sets
    "sell": "<markdown string>",
    "pass_mark": 80,
    "screens": [...],           # on translate_form and verbs sets
    "content": {...},
}
```

### 2b. Grammar screens (translate_form sets)
```python
"screens": [{
    "heading": "Node X: Tense Name",
    "body": "<markdown — MUST use left-to-right readable prose>",
    # NO body_align field — it defaults to left in the frontend
    "table": [
        {
            "conjugation": "I",
            "infinitive_ending": "-o",
            "example": "amo",
            "tr": "I love",             # translation — REQUIRED on tense tables
            "ep": [["stem",""], ["ending","blue"]]   # colour segments
        },
        ...
    ],
    "table_note": "<markdown colour key and notes>",
    "infinitive_ending_header": "Ending",
}]
```

**CRITICAL**: Do NOT add `"body_align":"left"` on screens — this was causing the right-to-left display bug. The frontend defaults correctly to left when the field is absent.

### 2c. Colour coding for `ep` segments
| Colour | Meaning |
|--------|---------|
| `""` (empty) | stem / neutral |
| `"coral"` | stem vowel / connecting vowel |
| `"blue"` | person ending |
| `"purple"` | past marker (-v-, -s-, -x-, or -ba- tense marker) |
| `"yellow"` | future marker (-bo-/-bi-/-bu- or -a-/-e-) |
| `"gold"` | pluperfect -era- marker |

### 2d. Verb list format (VERBS_Xth_TOP150)
```python
VERBS_Xth_TOP150 = [
    # (present, infinitive, perfect, ppp_or_None, eng_present, eng_infinitive, eng_perfect, eng_ppp)
    ("amo", "amare", "amavi", "amatus", "I love", "to love", "I loved", "having been loved"),
    ("festino", "festinare", "festinavi", None, "I hurry", "to hurry", "I hurried", None),
]
```

### 2e. Sentence format
```python
{
    "latin": "miles hostem petit.",           # always ends with period
    "english": [                              # ALWAYS a list, NEVER a string
        "the soldier seeks the enemy",
        "a soldier seeks the enemy",
        "the soldier is seeking the enemy",
        "a soldier is seeking the enemy",
        "the soldier attacks the enemy",      # include all valid meanings
        "a soldier attacks the enemy",
    ],
    "explanation": "**miles** = the soldier (nominative). **hostem** = the enemy (accusative). **petit** = he/she seeks (present, 3rd sg, from *peto*).",
}
```

### 2f. Explanation format (CRITICAL — currently broken in nodes 3–6)
- Use `**word**` (double asterisks = **bold**) for the Latin term being explained
- Use `*word*` (single asterisks = *italics*) for Latin words mentioned inline but not being the focus
- Use `. ` (period + space) to separate word entries — NOT `\n` (newline)
- End with a full stop
- Pattern: `"**latin_word** = english meaning (grammatical note, from *dictionary form*)."`
- Example from perfected Node 1:
  ```
  "**miles iratus** = the angry soldier. **reginam** = the queen (accusative). **rogavit** = he asked (perfect, from *rogo*)."
  ```
- **Node 3–6 currently use `*word*` and `\n` — this is WRONG and must be fixed to `**word**` and `. `**

### 2g. Valid answers — completeness requirements
Every sentence item's `english` list must include:
- With and without definite article ("the X" AND "a X") for every noun
- All valid tense translations (present: "loves" / "is loving"; imperfect: "was loving" / "used to love"; perfect: "loved" / "has loved")
- All 3rd-person gender variants if ambiguous (he/she/it)
- All valid meanings of polysemous words (e.g. peto: "seeks" / "attacks" / "begs" / "asks")
- PPP sentences: "having been ___-ed" form only (no passive: do not add "was ___-ed")

### 2h. Review set format
```python
"content": {
    "sentences": SENTENCES_REVIEW_Xth,    # 8–10 review sentences, all tenses
    "parse_translate": PARSE_TRANSLATE_Xth,  # 14–15 forms to parse + translate
}
```

---

## 3. LATIN ACCURACY RULES

### 3a. Prepositions
| Preposition | Governs | Rule |
|-------------|---------|------|
| **e / ex** | ablative | `e` before consonants (e.g. *e castris*, *e silva*); `ex` before vowels (e.g. *ex oppido*, *ex urbe*). For GCSE, *e castris* is the standard idiom — NOT *ex castris* |
| **a / ab** | ablative | `a` before consonants; `ab` before vowels/h (e.g. *a milite*, *ab hoste*) |
| **in + acc** | motion into | *in castra* = into the camp |
| **in + abl** | position in/on | *in castris* = in the camp |
| **ad** | accusative only | *ad castra* = towards the camp |
| **per** | accusative only | *per viam* = through the road |
| **post** | accusative only | *post bellum* = after the war |
| **ante** | accusative only | *ante proelium* = before the battle |
| **propter** | accusative only | *propter periculum* = because of the danger |
| **cum + abl** | ablative only | *cum militibus* = with the soldiers; **mecum, tecum, secum** (enclitic) |
| **prope** | accusative only | *prope silvam* = near the wood |

### 3b. Verb form accuracy
**3rd conjugation:**
- Present: -o, -is, -it, -imus, -itis, -unt (NOT -ant)
- Imperfect: -ēbam, -ēbas, -ēbat, -ēbamus, -ēbatis, -ēbant (connecting -e-)
- Future: -am, -ēs, -et, -ēmus, -ētis, -ent (NOT -bo/-bi/-bu)
- Perfect: must use the correct 3rd principal part stem (highly irregular — each verb individually)
- Pluperfect: perfect stem + -eram/-eras/-erat/-eramus/-eratis/-erant

**3rd -io verbs (facio, capio, accipio, cupio, effugio, conspicio):**
- Present: -io, -is, -it, -imus, -itis, -iunt (has -i- in they form unlike regular 3rd)
- Imperfect: -iēbam etc. (with -ie- not just -e-)
- Future: -iam, -iēs, -iet, -iēmus, -iētis, -ient (same as 4th conj)

**4th conjugation (audio, dormio, aperio, advenio):**
- Present: -io, -is (NOT -ies), -it, -imus, -itis, -iunt
- Imperfect: -iēbam etc.
- Future: -iam, -iēs, -iet, -iēmus, -iētis, -ient

**esse (sum):**
- Present: sum, es, est, sumus, estis, sunt
- Imperfect: eram, eras, erat, eramus, eratis, erant
- Future: ero, eris, erit, erimus, eritis, erunt
- Perfect: fui, fuisti, fuit, fuimus, fuistis, fuerunt
- Pluperfect: fueram, fueras, fuerat, fueramus, fueratis, fuerant
- Infinitive: esse; Future inf: futurum esse; perfect: fuisse

**possum:**
- Present: possum, potes, potest, possumus, potestis, possunt
- Imperfect: poteram, poteras, poterat, poteramus, poteratis, poterant
- Future: potero, poteris, poterit, poterimus, poteritis, poterunt
- Perfect: potui, potuisti, potuit, potuimus, potuistis, potuerunt
- Pluperfect: potueram etc.

**eo:**
- Present: eo, is, it, imus, itis, eunt
- Imperfect: ibam, ibas, ibat, ibamus, ibatis, ibant
- Future: ibo, ibis, ibit, ibimus, ibitis, ibunt
- Perfect: ii (or ivi), iisti, iit, iimus, iistis, ierunt
- Compounds: redeo (rediit, redire), abeo, exeo, pereo, transeo — all same pattern

### 3c. Noun/adjective agreement
- Adjectives agree with nouns in gender, number, AND case
- PPP agrees with the noun it describes in gender, number, and case (nominative when subject)
- Genitive singular: -ae (1st), -i (2nd), -is (3rd), -us (4th), -ei (5th)
- Never write "miles apertus" meaning "the soldier having been opened" — *aperio* PPP applied to a person requires the meaning "revealed/exposed/uncovered" to make sense

### 3d. Semantic sense-checking
Every sentence must make real-world sense:
- ✗ "pater apertus advenire poterat" — a father cannot be "opened"
- ✗ "rex capere oppugnatus est" — anachronistic passive construction
- ✓ "miles apertus ex domo effugit" — acceptable if "apertus" = "having been revealed/uncovered"
- All PPP sentences: check that the PPP meaning is semantically coherent with its referent noun

### 3e. Vocabulary restriction
**Only top-150 frequency words** may be used as tested vocabulary in exercises. Non-tested context words (prepositions, conjunctions, common nouns) may appear in sentences if they are recognisable from context or from the Sentence Vocabulary set.

---

## 4. TOP-150 VERB LIST BY CONJUGATION

### 1st Conjugation (13 verbs) ✓ ALREADY CORRECT
amo, festino, neco, navigo, rogo, libero, puto, appropinquo, clamo, impero, oro, habito, oppugno

### 2nd Conjugation (6 verbs) — MUST REMOVE 7 NON-TOP-150 VERBS
**KEEP:** video, teneo, habeo, appareo, persuadeo, iubeo
**REMOVE:** moneo, timeo, maneo, respondeo, rideo, sedeo, moveo
(None of these 7 appear in the top-150 word list)

### 3rd Conjugation Regular (11 verbs)
dico, duco, discedo, peto, quaero, cogo, relinquo, occido, cognosco, constituo, pono

### 3rd Conjugation -io (5 verbs)
facio, accipio, cupio, effugio, conspicio
(capio excluded as simplex — only accipio appears in top-150 as "accepi"; conspicio appears as "conspexi")

### Combined 3rd Conjugation Node (16 verbs total = ideal for 16-set node)
All 11 regular + all 5 -io = 16 verbs exactly

### 4th Conjugation (4 verbs)
audio, dormio, aperio, advenio
Note: advenio is a compound of venio (4th conj), not of eo (irregular)

### esse + possum (separate node)
sum/esse/fui, possum/posse/potui

### eo + compounds (separate node)
eo/ire/ii — core verb
redeo/redire/redii — in top-150 (rediit, redire)
Other compounds (abeo, exeo, pereo, transeo) — introduce as a family even if below top-150 frequency

---

## 5. GRAMMAR SCREEN WRITING STANDARDS

### Body text
- Write in plain prose, left-to-right, as if explaining to a bright 15-year-old
- Use `**bold**` for key terms and rules
- Use `*italics*` for Latin examples inline
- Use `\u00a0\u00a0\u00a0\u00a0` (non-breaking spaces) to indent example words
- Keep it concise: 3–5 lines of body before the table
- Do NOT add the "IMPORTANT:" all-caps warning style in body text (use bold instead)

### Table notes
- Always include colour key at the end
- Format: `**colour name** = description`
- List only colours actually used in that table's `ep` segments

### Grammar note for merged 3rd conjugation (Node 3)
The screen for "Present: 'I' Form" must include a reassuring note:
> "3rd conjugation verbs show some variety in their forms — especially in the 'I' form and in the perfect tense. Don't try to find a single rule: focus on learning each verb's principal parts individually. Some verbs end in *-io* in the first person (like *facio*, *capio*) — this is a natural variation within the 3rd conjugation family. The endings on the other five forms are the same."

The screen for "Present Tense Endings" must note the -io variation:
> "Some 3rd conjugation verbs have *-io* in the 'I' form and *-iunt* in the 'they' form. The remaining four forms (*-is, -it, -imus, -itis*) are the same for all 3rd conjugation verbs."

---

## 6. SENTENCE WRITING STANDARDS

### Quantity
- Each sentence set: exactly 10 sentences
- Review sentences: 8 sentences
- parse_translate: 14–15 forms

### Variety requirements
- Sentence vocabulary: vary the nouns and subjects — do not use *miles* in every sentence
- Spread across persons: use I/you/we forms occasionally, not just he/she/they
- Include at least 1 negative sentence per sentence set (non + verb)
- At least 2 sentences with preposition phrases per set
- PPP sentences: the noun the PPP describes must be clearly the subject or object — avoid ambiguity
- Do not repeat the same Latin sentence in different sets

### Noun pool by node
Use only nouns/adjectives defined in the Sentence Vocabulary set of that node plus inherited vocabulary from earlier nodes. Do not introduce new nouns without adding them to the vocab set.

---

## 7. KNOWN ERRORS TO FIX (running list)

### Preposition errors
- [ ] node3: `ex castris` → `e castris` (multiple occurrences — search & replace all)
- [ ] node3: Check all other `ex + consonant` cases
- [ ] node4: Check all preposition uses
- [ ] node5: Check all preposition uses

### Verb errors (non-top-150 in sentence explanations)
- [ ] node5 line ~390: `terreo` used as verb — replace with top-150 verb
- [ ] node5 line ~372: `respondeo` used — replace with top-150 verb

### Explanation format errors (nodes 3–6)
- [ ] All explanations use `*word*` + `\n` → must change to `**word**` + `. `

### Valid answer errors
- [ ] node5 review: `"the enemies were in the camp"` — only one answer listed, missing "a" article variant for each noun/other valid translations
- [ ] All sentence sets: audit for single-string `english` instead of list

### Structural errors
- [ ] Node 2: 7 non-top-150 verbs to remove; verb list to reduce from 13 to 6
- [ ] Node 3: Must merge with Node 4 (3rd -io) into single 16-set node
- [ ] Node 5: Must split into 4th Conjugation (16 sets) + esse/possum (new node)
- [ ] All node/node_title fields: update after renumbering
- [ ] _order in data.py: update after restructuring

---

## 8. BUILDING PARTS PATTERN SCREENS

### Infinitive pattern_screen template
```python
"pattern_screen": {
    "title": "Xth Conjugation: The Infinitive",
    "subtitle": "How to form it:",
    "examples": [
        {"present": "verb1", "full": "inf1", "ending": "suffix", "english": "to ..."},
        ...
    ],
    "footnote": "Notes on exceptions or special cases."
}
```

### Perfect pattern_screen template
```python
"pattern_screen": {
    "title": "Xth Conjugation: The Perfect",
    "subtitle": "Take the infinitive, remove -re, add [suffix]:",
    "examples": [
        {"full": "perf1", "ending": "vi", "inf": "inf1", "english": "I ...", "present": "pres1"},
        ...
    ],
    "footnote": "The [-marker-] is the past marker. Look for it to spot any perfect tense form."
}
```

### PPP pattern_screen template
```python
"pattern_screen": {
    "title": "Xth Conjugation: The PPP",
    "subtitle": "How the PPP is formed:",
    "examples": [
        {"present": "p1", "infinitive": "i1", "perfect": "pf1", "full": "ppp1", "ending": "tus", "english": "having been ..."},
        ...
    ],
    "footnote": "Note any verbs with no PPP. The PPP must agree in gender, number, and case with the noun it describes."
}
```

---

## 9. PUPIL JOURNEY SIMULATION — WHAT EACH NODE FEELS LIKE

A pupil working through a conjugation node should experience:
1. **Vocab set** (optional): Preview the supporting words they'll see in sentences
2. **PP1 verbs**: Learn the 'I' forms with meanings — feel of the conjugation family
3. **Present endings**: Grammar table with colour coding — understand the pattern
4. **Present sentences**: Apply it — translate real Latin sentences
5. **PP2 infinitive**: Learn "to..." form — principled derivation shown
6. **Imperfect**: New tense added — same coloured -ba- marker, now habitual
7. **Future**: Yet another marker — WARN clearly about 3rd/4th vs 1st/2nd difference
8. **Present system sentences**: Mix of all three — build fluency
9. **PP3 perfect**: Third part, highly irregular for 3rd conj — must memorise individually
10. **Perfect endings**: Same endings for all conjugations — feel of recognition
11. **Pluperfect**: Straightforward extension of perfect stem
12. **Perf/pluperf sentences**: Mix both past tenses
13. **PP4 PPP**: Fourth part — "having been ___-ed"
14. **PPP sentences**: Translate PPP in context — always "having been ___-ed"
15. **Build all parts**: Self-testing on all four — consolidation
16. **Review**: Full test — sentences (all tenses) + parse & translate

**Ghost testing check**: Before publishing a node, verify:
- No vocabulary appears in a sentence set that hasn't been introduced in that node's vocab set or a prior node
- No verb form is tested before its tense has been taught in that node
- No sentence requires knowledge from a later node's conjugation

---
