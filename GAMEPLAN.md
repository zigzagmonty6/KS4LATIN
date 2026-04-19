# Latin GCSE Platform — Restructuring Gameplan
## Complete Node Architecture & Edit Instructions

---

## PART A: NEW NODE ARCHITECTURE

### Full node map (proposed)

| Node | Title | Set IDs | Sets | Status |
|------|-------|---------|------|--------|
| 0 | Introduction | 1–4 | 4 | ✓ Keep as-is |
| 1 | 1st Conjugation (Top 150) | 5–20 | 16 | ✓ Perfected — do not touch |
| 2 | 2nd Conjugation (Top 150) | 21–36 | 16 | ⚠ Fix: remove 7 non-top-150 verbs + rebuild content |
| 3 | 3rd Conjugation (Top 150) | 37–52 | 16 | ⚠ Rebuild: merge current nodes 3+4 into one |
| 4 | 4th Conjugation (Top 150) | 53–68 | 16 | ⚠ Rebuild: extract from current node 5 |
| 5 | *esse* and *possum* | 69–84 | 16 | ⚠ Rebuild: extract esse/possum + add PPP+esse passive set |
| 6 | *eo* and Compounds | 85–100 | 16 | 🆕 New node |
| 7 | *volo*, *conor*, *coepi* | 101–104 | 4 | 🆕 Mini-node |
| 8 | Consolidation | 105–120 | 16 | ⚠ Rebuild: restructure to match new node map |

**Total: 120 sets** (up from 100)

### 3rd Conjugation -io verbs — CONFIRMED LIST (no capio)
Only verbs explicitly present in top-150 as their own entry or via a distinctive perfect form:
- facio (feci in top-150 ✓)
- accipio (accepi in top-150 ✓)
- cupio (cupio in top-150 ✓)
- effugio (effugio in top-150 ✓)
- conspicio (conspexi in top-150 ✓)
capio excluded: only appears implicitly via accipio; teaching capio separately would introduce a word not in the prescribed list.

### Set ID renumbering plan

| Old ID range | Old content | New ID range | New content |
|---|---|---|---|
| 1–4 | Introduction | 1–4 | Introduction (unchanged) |
| 5–20 | Node 1: 1st Conjugation | 5–20 | Node 1: 1st Conjugation (unchanged) |
| 21–36 | Node 2: 2nd Conjugation | 21–36 | Node 2: 2nd Conjugation (fixed) |
| 37–52 | Node 3: 3rd Conjugation (regular only) | 37–52 | Node 3: 3rd Conjugation (merged 3rd + -io) |
| 53–68 | Node 4: 3rd -io Conjugation | 53–68 | Node 4: 4th Conjugation (moved from old node 5) |
| 69–84 | Node 5: 4th Conj + esse/possum | 69–84 | Node 5: esse + possum (new) |
| 85–100 | Node 6: Consolidation | 85–100 | Node 6: eo + compounds (new) |
| — | — | 101–116 | Node 7: Other irregulars (new) |
| — | — | 117–132 | Node 8: Consolidation (rebuilt) |

---

## PART B: NODE-BY-NODE EDIT INSTRUCTIONS

---

### NODE 2: 2nd Conjugation — Fix verb list

**Problem:** Current VERBS_2ND_TOP150 has 13 verbs. 7 are NOT in the top-150 frequency list.

**Remove these 7 verbs:**
- moneo (warn) — not in top-150
- timeo (fear) — not in top-150
- maneo (remain) — not in top-150
- respondeo (reply) — not in top-150
- rideo (laugh) — not in top-150
- sedeo (sit) — not in top-150
- moveo (move) — not in top-150

**Keep these 6 verbs:**
1. video, videre, vidi, visus — I see
2. teneo, tenere, tenui, tentus — I hold
3. habeo, habere, habui, habitus — I have
4. appareo, apparere, apparui, None — I appear
5. persuadeo, persuadere, persuasi, None — I persuade
6. iubeo, iubere, iussi, iussus — I order

**Consequential edits required:**
- Rewrite QUESTIONS_PRESENT (only use above 6 verbs)
- Rewrite QUESTIONS_IMPERFECT (only above 6)
- Rewrite QUESTIONS_FUTURE (only above 6)
- Rewrite QUESTIONS_PERFECT (only above 6)
- Rewrite QUESTIONS_PLUPERFECT (only above 6)
- Rewrite all Node 2 sentence sets (SENTENCES_*): remove any sentences using non-top-150 verbs
- Review NODE2_VOCAB: keep only supporting words
- Fix all explanation formats: *word* + \n → **word** + period

**Grammar screen notes for 2nd conjugation:**
- Present: -eo, -es, -et, -emus, -etis, -ent (the -e- stem vowel persists)
- Imperfect: -ebam etc. (same -ba- as 1st, with -e- stem vowel)
- Future: -ebo, -ebis, -ebit, -ebimus, -ebitis, -ebunt (uses -bo/-bi like 1st but with -e- stem)
- Perfect: varies — -ui (habui, tenui, apparui), -si (persuasi, iussi), -di (vidi has changed stem)
- Warn: "vidi" looks like it could be perfect of "video" but has a completely changed stem — learn it specially

---

### NODE 3: 3rd Conjugation — Merge 3rd + 3rd-io

**Problem:** Currently two separate nodes (old 3 = regular, old 4 = -io). Must become one 16-set node covering all 16 top-150 3rd conjugation verbs.

**New verb list (VERBS_3RD_TOP150 — 16 verbs):**

Regular 3rd (11):
1. dico, dicere, dixi, dictus — I say
2. duco, ducere, duxi, ductus — I lead
3. discedo, discedere, discessi, None — I depart
4. peto, petere, petivi, petitus — I seek / beg / attack
5. quaero, quaerere, quaesivi, quaesitus — I search for
6. cogo, cogere, coegi, coactus — I force
7. relinquo, relinquere, reliqui, relictus — I leave (behind)
8. occido, occidere, occidi, occisus — I kill
9. cognosco, cognoscere, cognovi, cognitus — I find out
10. constituo, constituere, constitui, constitutus — I decide
11. pono, ponere, posui, positus — I put

-io variants (5):
12. facio, facere, feci, factus — I make / do
13. accipio, accipere, accepi, acceptus — I receive / accept
14. cupio, cupere, cupivi, cupitus — I want / desire
15. effugio, effugere, effugi, None — I escape
16. conspicio, conspicere, conspexi, conspectus — I notice / catch sight of
    (in top-150 as "conspexi")

**Grammar screen approach for the -io variation:**

In the "Present: 'I' Form" screen add:
> "Most 3rd conjugation verbs end in just *-o* in the 'I' form (*dico*, *duco*, *peto*). A few end in *-io* (*facio*, *accipio*, *cupio*, *effugio*, *conspicio*) — this is a natural variation. Don't worry about why: simply learn each verb's forms as you encounter them. The principal parts will tell you everything you need."

In the "Present Tense Endings" screen add a note about -io variants:
> "The four middle forms (*-is, -it, -imus, -itis*) are the same for ALL 3rd conjugation verbs. The *-io* verbs have *-iunt* in the 'they' form (like *faciunt*) — the others have *-unt* (like *dicunt*)."

Show TWO rows in the table to illustrate both patterns:
- *dico* family: dic-o, dic-is, dic-it, dic-imus, dic-itis, dic-unt
- *facio* family: faci-o, faci-s, faci-t, faci-mus, faci-tis, faci-unt

**Existing content to reuse:**
- VERBS_3RD_TOP150 (11 verbs) → keep
- All QUESTIONS_*_3RD → keep
- All SENTENCES_*_3RD → keep (fix Latin errors first)
- VERBS_3RD_IO_TOP150 (5 verbs) → merge into VERBS_3RD_TOP150
- All QUESTIONS_*_3RD_IO → merge into question pools
- All SENTENCES_*_3RD_IO → merge into sentence pools
- NODE3_VOCAB + NODE4_VOCAB → merge, deduplicate

**Latin errors to fix in Node 3:**
- `ex castris` → `e castris` (multiple occurrences — grep for all)
- Check: `dux milites ex castris ducit` → `dux milites e castris ducit`
- Check all other prepositions in node3_data.py and node4_data.py
- Fix ALL explanation formats: `*word*\n` → `**word** = ... . `

**Sentence vocabulary for merged node 3:**
Merge NODE3_VOCAB and NODE4_VOCAB, keeping only top-150 relevant nouns:
- From NODE3: puer, pater, mater, frater, hostis, bellum, periculum, iter, castra, omnis, clarus, iam, tandem, cum (+ abl)
- From NODE4: arma, porta, flumen, cibus, mons, vulnus, nuntius, gravis, deinde, tum, post (+acc), propter
- Drop: saepe, numquam (not in top-150 — check)

**New _order for Node 3 (sets 37–52):**
Vocab first (id=37), then: 38(verbs), 39(present_endings), 40(present_sent), 41(infinitive), 42(imperfect), 43(future), 44(present_system), 45(perfect_pp3), 46(perfect_endings), 47(pluperfect), 48(perf_pluperf_sent), 49(PPP), 50(PPP_sent), 51(build_parts), 52(review)

---

### NODE 4: 4th Conjugation — New standalone node

**Reassign IDs 53–68 (formerly 3rd -io node)**

**Verb list (4 verbs — same as existing VERBS_4TH_TOP150):**
1. audio, audire, audivi, auditus — I hear
2. dormio, dormire, dormivi, None — I sleep
3. aperio, aperire, aperui, apertus — I open
4. advenio, advenire, adveni, None — I arrive

Note: Only 4 verbs, but that is fine — sets test all forms of each, and 10 sentences are achievable.

**Grammar screens to write:**
- Present: -io, -is, -it, -imus, -itis, -iunt (the -i- is present throughout)
- Imperfect: -iebam etc. (same -ie- as 3rd -io)
- Future: -iam, -ies, -iet, -iemus, -ietis, -ient (same as 3rd -io)
- Perfect: varies (-avi for audio/dormio; -ui for aperio; -i for advenio)
- Note: aperio perfect is aperui (not aperivi) — -u- marker
- Note: advenio perfect is adveni — effectively a stem change

**Content to reuse from current node5_data.py:**
- VERBS_4TH_TOP150 → keep as Node 4 verb list
- NODE5_VOCAB → becomes Node 4 Sentence Vocabulary (remove esse/possum-specific vocab)
- All QUESTIONS_*_4TH → keep
- All SENTENCES_*_4TH → keep (audit for Latin errors)
- PARSE_TRANSLATE_4TH → keep

**Latin errors to check in 4th conjugation content:**
- `miles apertus ex domo effugit` — check: "ex domo" is acceptable (domus starts with 'd' but ex before consonants is valid for domus idiomatically); however "e domo" would be more classical
- "respondere" used in sentence (non-top-150) → replace verb
- "terreo" used in explanation → replace with top-150 verb (audio/advenio/pono)
- Check all other prepositions

**Node title:** "4th Conjugation (Top 150)"
**Node_title field:** "4th Conjugation (Top 150)"

---

### NODE 5: *esse* and *possum* — New standalone node (16 sets)

**Node title:** "*esse* and *possum*"
**IDs: 69–84**

**Verb coverage:**
- sum, esse, fui (I am / to be / I was)
- possum, posse, potui (I am able / to be able / I was able)

No PPP for either verb.

**Proposed 16-set structure:**

| Set | Title | Type | Content |
|-----|-------|------|---------|
| 69 | Sentence Vocabulary | vocab | Nouns/adjectives to use in esse/possum sentences |
| 70 | *sum*: All Present Forms | translate_form | est, sunt, sum, es, etc. |
| 71 | *sum*: Past Tenses | translate_form | erat, erant, fuit, fuerant |
| 72 | *sum*: Future | translate_form | ero, erit, erunt |
| 73 | *sum* in Sentences | sentences | 10 sentences with est/erat/erit/fuit |
| 74 | *possum*: All Present Forms | translate_form | possum, potes, potest, etc. |
| 75 | *possum*: Past Tenses | translate_form | poterat, potuerunt, potuerat |
| 76 | *possum*: Future | translate_form | potero, poterit, poterunt |
| 77 | *possum* in Sentences | sentences | 10 sentences with possum + infinitive |
| 78 | *esse* as Linking Verb | sentences | Predicate adjective sentences (rex bonus est) |
| 79 | *esse* + PPP Constructions | sentences | Passive with esse (optional at GCSE) |
| 80 | Combined: *sum* + *possum* | sentences | Sentences using both |
| 81 | Principal Parts of *esse* | building_parts | sum / esse / fui (no PPP) |
| 82 | Principal Parts of *possum* | building_parts | possum / posse / potui (no PPP) |
| 83 | Build Both Verbs | building_parts | Both verbs, all parts tested |
| 84 | Review | review | Sentences + parse_translate covering both verbs |

**Grammar screen content for esse:**
> "*sum* is the most irregular verb in Latin — but also the most common. Its forms must be memorised individually. You will see *est* (he/she/it is) and *erant* (they were) on almost every GCSE paper."

Show the full present tense table with colour coding (no stem vowel to highlight):
sum | es | est | sumus | estis | sunt

**Imperfect of esse:** eram/eras/erat/eramus/eratis/erant (note: -era- looks like pluperfect marker — explain)
**Future of esse:** ero/eris/erit/erimus/eritis/erunt
**Perfect:** fui (completely different stem — note this)
**Pluperfect:** fueram etc.

---

### NODE 6: *eo* and Compounds — New standalone node (16 sets)

**Node title:** "*eo* and Compounds"
**IDs: 85–100**

**Verb coverage:**
- eo, ire, ii — I go (core verb, highly irregular)
- redeo, redire, redii — I return (in top-150 as rediit/redire)
- abeo, abire, abii — I go away
- exeo, exire, exii — I go out
- pereo, perire, perii — I die / perish (poetically common)
- transeo, transire, transii — I cross

**Approach:** Teach eo first, then introduce compounds as a family. Emphasis: once you know eo, all compounds follow the same pattern.

**Proposed 16-set structure:**

| Set | Title | Type | Content |
|-----|-------|------|---------|
| 85 | Sentence Vocabulary | vocab | Vocabulary for eo contexts (locus, iter, via, etc.) |
| 86 | *eo*: Present Tense | translate_form | eo, is, it, imus, itis, eunt |
| 87 | *eo*: Imperfect and Future | translate_form | ibam/ibas/ibat + ibo/ibis/ibit |
| 88 | *eo*: Perfect and Pluperfect | translate_form | ii/iit/ierunt + ierat/ierant |
| 89 | *eo* in Sentences | sentences | 10 sentences using eo in various tenses |
| 90 | *redeo*: Introduction | translate_form | Present + imperfect of redeo |
| 91 | *redeo* in Sentences | sentences | 10 sentences with redeo |
| 92 | Compounds: *abeo*, *exeo* | translate_form | Present + perfect of abeo, exeo |
| 93 | Compounds in Sentences | sentences | 10 sentences with abeo/exeo/pereo |
| 94 | *eo* + Infinitive Constructions | sentences | Sentences with eo + purpose clause (ad + gerund, or bare inf) |
| 95 | Principal Parts of *eo* | building_parts | eo / ire / ii (no PPP) |
| 96 | Principal Parts: Compounds | building_parts | All 5 compounds, all parts |
| 97 | Mixed *eo* Family | sentences | 10 sentences mixing all eo compounds |
| 98 | Build the Compounds | building_parts | Gap-fill on all compound principal parts |
| 99 | Parse *eo* Forms | translate_form | iit, ibant, iero, ierant, redibat, exiit etc. |
| 100 | Review | review | Mixed sentences + parse_translate |

---

### NODE 7: *volo*, *conor*, *coepi* — Mini-node (4 sets only)

**Node title:** "Other Key Verbs"
**IDs: 101–104**

**Rationale:** Deponent verbs broadly are being saved for a later vocabulary/forms node. This node covers only the three specific top-150 irregular verbs that do not belong in any regular conjugation node. Kept deliberately short — these are revision pupils filling gaps, not learning from scratch.

**Verb coverage (top-150 only):**
- volo/nolo — I want / I don't want (volo, vis, vult; nolo, non vis, non vult; noli + inf)
- conor — I try (deponent: conatur appears in top-150)
- coepi — I began (defective: perfect system only; coepi + infinitive is the key construction)

**4-set structure:**

| Set | Title | Type | Content |
|-----|-------|------|---------|
| 101 | *volo* and *nolo* | translate_form | All forms of volo + nolo; noli + inf for prohibitions |
| 102 | *conor* and *coepi* | translate_form | conatur/conabantur + coepi/coeperat |
| 103 | These Verbs in Sentences | sentences | 10 sentences mixing volo/nolo/conor/coepi |
| 104 | Review | review | Short review: 6 sentences + 8 parse_translate |

---

### NODE 8: Consolidation — Rebuilt (16 sets)

**Node title:** "Consolidation"
**IDs: 105–120**

**Old → new content mapping:**

| Old Set | Old Title | Action |
|---------|-----------|--------|
| 85 | Sentence Vocabulary (consolidation) | → becomes Set 117, update vocab |
| 86 | Present: All Conjugations | → becomes Set 118 |
| 87 | Present System: Mixed Sentences | → becomes Set 119 |
| 88 | Perfect + Pluperfect: All | → becomes Set 120 |
| 89 | Perfect System: Mixed Sentences | → becomes Set 121 |
| 90 | Tense Identification | → becomes Set 122 |
| 91 | Parsing Practice | → becomes Set 123 |
| 92 | Complex Sentences | → becomes Set 124 |
| 93 | PPP Sentences: All Conjugations | → becomes Set 125 |
| 94 | Mixed Sentences I | → becomes Set 126 |
| 95 | Mixed Sentences II | → becomes Set 127 |
| 96 | 1st vs 2nd Conjugation Review | → becomes Set 128, retitle "1st & 2nd Conjugation Review" |
| 97 | 3rd Conjugation Review | → becomes Set 129 (now covers all 16 verbs incl. -io) |
| 98 | 3rd -io & 4th Conjugation Review | → becomes Set 130, retitle "4th Conjugation Review" |
| 99 | Comprehensive Parsing | → becomes Set 131, add esse/possum/eo forms |
| 100 | Final Review | → becomes Set 132, broaden to all 8 nodes |

**Ghost-testing audit for Consolidation:**
Before writing consolidation sentences, check:
- No sentence uses a verb from a conjugation not yet introduced in that set's intended scope
- Sentences labelled "3rd Conjugation Review" use ONLY 3rd conj verbs (including -io variants)
- "4th Conjugation Review" uses ONLY audio/dormio/aperio/advenio
- "Final Review" may use ALL top-150 verbs but must label each verb source clearly in explanation

---

## PART C: SYSTEMATIC LATIN AUDIT INSTRUCTIONS

### Step 1: e/ex audit
```
Search all node files for "ex " followed by a consonant:
ex c, ex d, ex f, ex g, ex h (exception: h is usually aspirate, ex fine), ex l, ex m, ex n, ex p, ex r, ex s, ex t, ex v
Standard GCSE idioms that MUST use "e":
  e castris (from the camp)
  e silva (from the wood)
  e via (from the road)
  e nave (from the ship — but navis starts with n → "e nave" ✓)
Standard cases that MUST use "ex":
  ex oppido (from the town — vowel)
  ex urbe (from the city — vowel)
  ex agro (from the field — vowel)
```

### Step 2: a/ab audit
```
Check all preposition phrases:
"a + consonant" ✓ (a milite, a rege)
"ab + vowel" ✓ (ab oppido, ab hoste)
"a + vowel" ✗ → change to "ab"
"ab + consonant" → acceptable but "a" preferred in GCSE texts
```

### Step 3: Verb form audit
```
For every verb form in QUESTIONS_* arrays, verify:
- The form is built correctly from the correct principal part
- 3rd conj future uses -am/-es/-et (NOT -bo/-bi)
- 3rd -io imperfect uses -iebam (NOT -ebam without -i-)
- 4th imperfect uses -iebam (NOT -ebam)
- Perfect stems match principal part 3
- Pluperfect = perfect stem + -eram (NOT present stem + -eram)
```

### Step 4: Semantic sense audit
```
For every sentence:
- Subject and object must be semantically compatible
- PPP must logically apply to the noun it modifies
- Verb must take the correct case (transitive with accusative, intransitive without)
- Check: no "soldier opened" (apertus applied to animate being without metaphorical sense)
- Check: no inanimate subject with experiencer verb
```

### Step 5: Explanation format audit
```
For every sentence explanation, verify:
- Uses **bold** (double asterisks) for Latin terms being explained, NOT *italics*
- Entries separated by ". " (period-space), NOT "\n"
- Ends with a full stop
- Grammatical notes in parentheses: "(accusative)", "(perfect, 3rd sg, from *verb*)"
- Verb parsing format: "(tense, person number, from *dictionary_form*)"
  e.g. "(perfect, 3rd sg, from *dico*)" NOT "(perfect, he/she form, from *dico*)"
```

### Step 6: Valid answers audit
```
For every sentence, english list must contain:
- "the [noun]..." AND "a [noun]..." for all singular nouns that are subjects
- All valid tense translations:
  - present: "X-s" / "is X-ing"
  - imperfect: "was X-ing" / "used to X" / "kept X-ing"
  - perfect: "X-ed" / "has X-ed"
  - pluperfect: "had X-ed"
- All meanings of polysemous verbs:
  - peto: seeks / attacks / begs / asks
  - relinquo: leaves / leaves behind / abandons
  - cognosco: finds out / gets to know / discovers / recognises
  - dico: says / tells
  - duco: leads / takes / brings
  - facio: makes / does
  - accipio: receives / accepts
  - quaero: searches for / asks (for) / seeks
  - constituo: decides / resolves / establishes
```

---

## PART D: IMPLEMENTATION ORDER

### Phase 1: Fix Node 2 (2nd Conjugation)
1. Update VERBS_2ND_TOP150 (remove 7 verbs)
2. Rewrite all QUESTIONS_* arrays (only 6 verbs)
3. Audit and fix all sentences (remove non-top-150 verb usage)
4. Fix all explanation formats
5. Run syntax check + runtime validation

### Phase 2: Fix Node 3 (Merge 3rd + 3rd-io)
1. Merge VERBS_3RD_TOP150 + VERBS_3RD_IO_TOP150 into single list (16 verbs)
2. Merge all QUESTIONS_* arrays
3. Merge NODE3_VOCAB + NODE4_VOCAB
4. Fix all ex→e errors throughout
5. Fix all explanation formats
6. Update grammar screens (add -io variation note)
7. Merge sentence sets
8. Update NODE3_SETS IDs and node fields
9. Delete NODE4_SETS entirely
10. Reassign old node 4 IDs (53–68) to new 4th conjugation node

### Phase 3: Build Node 4 (4th Conjugation standalone)
1. Rename VERBS_4TH_TOP150, NODE5_VOCAB, QUESTIONS_*_4TH → node 4 naming
2. Update all set IDs from 69–84 range to 53–68
3. Update node field from 5 → 4, node_title to "4th Conjugation (Top 150)"
4. Remove esse/possum content from this node's sentences
5. Write new grammar screens for 4th conj (currently bundled with esse/possum)
6. Audit Latin errors
7. Fix explanation formats

### Phase 4: Build Node 5 (esse + possum standalone)
1. Write new 16-set structure from scratch
2. Write all grammar screens for esse and possum
3. Write all question arrays
4. Write all sentence sets
5. Write parse_translate review

### Phase 5: Build Node 6 (eo + compounds)
1. Write all grammar screens for eo
2. Write all question arrays (present, imperfect, future, perfect, pluperfect)
3. Write all sentence sets for eo and each compound
4. Write parse_translate review

### Phase 6: Build Node 7 (Other irregulars)
1. Write volo grammar screens and questions
2. Write nolo content (shares most forms with volo)
3. Write conor introduction and questions
4. Write coepi introduction and questions
5. Mixed sentences + review

### Phase 7: Rebuild Node 8 (Consolidation)
1. Map old set IDs 85–100 to new 117–132
2. Update node and node_title fields
3. Redesign review sets to cover all 8 nodes
4. Ghost-test all sentences

### Phase 8: Update data.py assembly
1. Update reconstruct_and_merge.py or write new assembly script
2. Update _order array to cover all 132 sets
3. Update SETS_BY_ID
4. Run syntax check + full runtime validation
5. Verify: 132 sets, IDs 1–132, no missing IDs

---

## PART E: REMAINING DECISIONS NEEDED

Before Phase 4 (esse/possum) work begins:

**Q1: esse passive constructions?**
At GCSE, students sometimes see "amatus est" (he was loved) = PPP + esse in passive voice. Should Node 5 introduce this, or leave it to consolidation?
→ Recommendation: include one set on "PPP + esse" as it is tested at GCSE

**Q2: eo compounds in top-150?**
Only "rediit/redire" explicitly appears. Should abeo/exeo/pereo/transeo be introduced even though they're below top-150 frequency?
→ Recommendation: yes, teach as a pattern family — knowing eo means you get all compounds free

**Q3: conspicio vs capio?**
Current node 4 uses "capio" (take). The top-150 has "accepi" (= accipio) but also "conspexi" (= conspicio). Should the merged node 3 drop capio in favour of conspicio, or use both?
→ Recommendation: drop capio (not explicitly in top-150 as simplex); use accipio + conspicio instead. The 5 -io verbs are: facio, accipio, cupio, effugio, conspicio

**Q4: Node 7 scope?**
Should "Other Key Verbs" also include common deponent verbs like loquor (I speak), proficiscor (I set out), if they appear in the exam texts beyond what is strictly top-150?
→ Need your input

---

## PART F: PUPIL JOURNEY — GHOST TESTING SIMULATION

Simulate a pupil starting at Node 0 and working through to Node 8:

**Node 0 → Node 1:** Pupil learns verbs only. No nouns tested yet. ✓

**Node 1 → Node 2:** Pupil enters Node 2.
- Check: Node 2 sentences use only 1st-conj verbs (already known) + 2nd-conj verbs (being learned).
- GHOST TEST: Any 3rd, 4th, or irregular verb in Node 2 sentences is a cognitive blocker. ✗ Flag and replace.

**Node 2 → Node 3:** Pupil enters merged 3rd conjugation.
- Check: Node 3 sentences may use 1st + 2nd + 3rd conj verbs. No 4th or irregular.
- GHOST TEST: Any 4th conj verb (audio, dormio, aperio, advenio) in Node 3 is a blocker. ✗ Flag.

**Node 3 → Node 4:** Pupil enters 4th conjugation.
- Node 4 sentences may use 1st + 2nd + 3rd + 4th conj verbs.
- GHOST TEST: Any esse/possum in Node 4 sentences as the main verb being tested = blocker.
  (esse/possum as supporting verbs "could be" OK if used naturally, but flag for review)

**Node 4 → Node 5:** Pupil enters esse/possum.
- Node 5 may use ANY regular conjugation verb + esse + possum.
- GHOST TEST: Any eo/volo/conor form in Node 5 = blocker. ✗ Flag.

**Node 5 → Node 6:** Pupil enters eo + compounds.
- Node 6 may use everything learned so far + eo family.
- GHOST TEST: Any volo/conor/coepi form in Node 6 = blocker.

**Node 6 → Node 7:** Pupil enters other irregulars.
- Node 7 may use all previous verbs + volo/nolo/conor/coepi.

**Node 7 → Node 8:** Pupil enters Consolidation.
- All verbs from all nodes now fair game.
- GHOST TEST: Sentences labelled as "3rd Conjugation Review" should use ONLY 3rd conj verbs + any supporting grammar already known.

---
