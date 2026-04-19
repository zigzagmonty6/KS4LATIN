import re

with open('data.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace em-dashes
text = text.replace('—', '-')

# Define the new sets
new_sets_str = """SETS = [
    # -- Node 0: Introduction --------------------------------------------------
    {
        "id":1, "node":0, "node_title":"Introduction",
        "title":"What is a Verb?",
        "type":"reference", "optional":True,
        "sell": 'A verb is a **doing**, **being** or **having** word.\\n\\nIn Latin the verb almost always comes **last**:\\n\\n*miles nautam necat.* - the soldier kills the sailor.\\n\\n*necat* (kills) is last. In English it comes second.',
        "pass_mark":None,
    },
    {
        "id":2, "node":0, "node_title":"Introduction",
        "title":"What are Principal Parts?",
        "type":"reference", "optional":True,
        "sell": 'Every Latin verb has up to four dictionary forms: the **principal parts**.\\n\\n**1st** *amo* - present - I love\\n**2nd** *amare* - infinitive - to love\\n**3rd** *amavi* - perfect - I loved\\n**4th** *amatus* - PPP - having been loved\\n\\nLearn all four. They are the key to every tense you will meet in the exam, They unlock every tense in the exam.',
        "pass_mark":None,
    },
    {
        "id":3, "node":0, "node_title":"Introduction",
        "title":"What are Conjugations?",
        "type":"reference", "optional":True,
        "sell": 'A conjugation is **a family of verbs** that share the same endings.\\n\\n**1st** - infinitive *-are* - *amo / amare*\\n**2nd** - infinitive *-ere* - *habeo / habere*\\n**3rd** - infinitive *-ere* - *duco / ducere*\\n**4th** - infinitive *-ire* - *audio / audire*',
        "pass_mark":None,
        "footnote":"2nd and 3rd look the same. Check the present tense: -eo = 2nd; -o (no -e) = 3rd.",
    },
    {
        "id":4, "node":0, "node_title":"Introduction",
        "title":"What is Parsing?",
        "type":"reference", "optional":True,
        "sell": 'Parsing means identifying what a Latin verb form tells you:\\n\\n**Tense** - *when* is the action happening?\\n**Person** - *who* is doing it? (3rd = he/she/they)\\n**Number** - *how many*? (singular / plural)\\n\\n*amavit* → perfect, 3rd singular → **he/she loved**\\n*amant* → present, 3rd plural → **they love**',
        "pass_mark":None,
    },

    # -- Node 1: 1st Conjugation Top 150 --------------------------------------
    {
        "id":5, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentence Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"The nouns, adjectives and prepositions that appear in the sentences later in this node.",
        "pass_mark":80,
        "content":{"vocab":NODE1_VOCAB, "mode":"meanings"},
    },
    {
        "id":6, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Present Tense",
        "type":"vocab",
        "sell":"The 13 most frequent 1st conjugation verbs from the GCSE list. Learn what each one means.",
        "pass_mark":80,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"meanings"},
    },
    {
        "id":7, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Present Tense Endings",
        "type":"building_parts",
        "sell":"The present tense endings are **-t** (he/she/it) and **-nt** (they). Let's learn these forms.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150, "mode":"present_endings", "show_parts_so_far":1,
            "pattern_screen":{
                "heading":"1st Conjugation: Present Tense Endings",
                "rule":"Take the present stem (amo -> ama-) and add the endings:",
                "examples":[
                    {"present":"amo",    "stem":"ama",    "ending":"t","full":"amat",    "english":"he/she loves"},
                    {"present":"amo",    "stem":"ama",    "ending":"nt","full":"amant",   "english":"they love"},
                    {"present":"neco",   "stem":"neca",   "ending":"t","full":"necat",    "english":"he/she kills"},
                    {"present":"neco",   "stem":"neca",   "ending":"nt","full":"necant",   "english":"they kill"},
                ],
                "note":"GCSE mainly tests the 3rd person singular (-t) and plural (-nt).",
            },
        },
    },
    {
        "id":8, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: Present",
        "type":"sentences",
        "sell":"Translate these sentences into English. All verbs are in the present tense.",
        "pass_mark":80,
        "content":{"sentences":[s for s in NODE1_SENTENCES if "rogo" in s["explanation"] or "oro" in s["explanation"] or "impero" in s["explanation"] or "oppugno" in s["explanation"] and "present" in s["explanation"]]},
    },
    {
        "id":9, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Infinitives",
        "type":"building_parts",
        "sell":"The infinitive adds **-re** to the stem. For 1st conjugation verbs the stem ends in *-a-*, so the infinitive always ends in *-are*.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150, "mode":"infinitives", "show_parts_so_far":1,
            "pattern_screen":{
                "heading":"1st Conjugation: Infinitive",
                "rule":"Add **-re** to the stem:",
                "examples":[
                    {"present":"amo",    "stem":"am",    "ending":"re","full":"amare",    "english":"to love"},
                    {"present":"rogo",   "stem":"rog",   "ending":"re","full":"rogare",   "english":"to ask"},
                    {"present":"neco",   "stem":"nec",   "ending":"re","full":"necare",   "english":"to kill"},
                    {"present":"navigo", "stem":"navig", "ending":"re","full":"navigare", "english":"to sail"},
                    {"present":"festino","stem":"festin","ending":"re","full":"festinare","english":"to hurry"},
                ],
                "note":"Every 1st conjugation verb ends in *-are*. The *-a-* before the *-re* is the signature of the 1st conjugation.",
            },
        },
    },
    {
        "id":10, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfects",
        "type":"building_parts",
        "sell":"The perfect tense describes a **completed action** in the past. For 1st conjugation, the past marker is **-v-** and the 1st person singular ends *-vi*.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150, "mode":"perfects", "show_parts_so_far":2,
            "pattern_screen":{
                "heading":"1st Conjugation: Perfect",
                "rule":"Take the infinitive, remove the *-re*, add *-vi*:",
                "examples":[
                    {"present":"amo",    "stem":"ama",    "ending":"vi","full":"amavi",    "inf":"amare",    "english":"I loved"},
                    {"present":"rogo",   "stem":"roga",   "ending":"vi","full":"rogavi",   "inf":"rogare",   "english":"I asked"},
                    {"present":"neco",   "stem":"neca",   "ending":"vi","full":"necavi",   "inf":"necare",   "english":"I killed"},
                    {"present":"navigo", "stem":"naviga", "ending":"vi","full":"navigavi", "inf":"navigare", "english":"I sailed"},
                    {"present":"festino","stem":"festina","ending":"vi","full":"festinavi","inf":"festinare","english":"I hurried"},
                ],
                "note":"The **-v-** is the past marker. Other endings: *-vit* = he/she; *-verunt* = they. Look for the *-v-* to spot a perfect tense form.",
            },
        },
    },
    {
        "id":11, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: Past & Present",
        "type":"sentences",
        "sell":"Translate these sentences containing imperfect and perfect tenses.",
        "pass_mark":80,
        "content":{"sentences":[s for s in NODE1_SENTENCES if "imperfect" in s["explanation"] or "perfect" in s["explanation"]]},
    },
    {
        "id":12, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect Passive Participles",
        "type":"building_parts",
        "sell":"The PPP means 'having been done'. Take the infinitive, remove *-re*, add *-tus*.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150, "mode":"ppps", "show_parts_so_far":3,
            "pattern_screen":{
                "heading":"1st Conjugation: PPP",
                "rule":"Take the infinitive, remove the *-re*, add *-tus*:",
                "examples":[
                    {"present":"amo",    "stem":"ama",   "ending":"tus","full":"amatus",   "inf":"amare",   "english":"having been loved"},
                    {"present":"rogo",   "stem":"roga",  "ending":"tus","full":"rogatus",  "inf":"rogare",  "english":"having been asked"},
                    {"present":"neco",   "stem":"neca",  "ending":"tus","full":"necatus",  "inf":"necare",  "english":"having been killed"},
                    {"present":"libero", "stem":"libera","ending":"tus","full":"liberatus","inf":"liberare","english":"having been freed"},
                    {"present":"oppugno","stem":"oppugna","ending":"tus","full":"oppugnatus","inf":"oppugnare","english":"having been attacked"},
                ],
                "note":"*festino*, *navigo* and *appropinquo* have no PPP in the dictionary - you will see this in the next set.",
            },
        },
    },
    {
        "id":13, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Fill the Missing Part",
        "type":"building_parts",
        "sell":"You will see three Principal Parts. Type the missing part in the blank.",
        "pass_mark":80,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":14, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"All Four Parts",
        "type":"building_parts",
        "sell":"You see only the present tense. Type the other parts in order, separated by spaces or slashes.",
        "pass_mark":80,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"all_four_from_present", "show_parts_so_far":4},
    },
    {
        "id":15, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Translate the Form",
        "type":"translate_form",
        "sell":"A Latin form appears. Choose the correct English meaning. Options are always in the same order: 1 = present, 2 = infinitive, 3 = perfect, 4 = PPP.",
        "pass_mark":80,
        "content":{"questions":TRANSLATE_FORM_QUESTIONS},
    },
    {
        "id":16, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Recognising Tenses",
        "type":"tense_id",
        "sell":("Identify the tense of each verb form. Five tenses - look at the endings.\\n\\n"
                "**Present**: *-t* (he/she), *-nt* (they)\\n"
                "**Imperfect**: *-bat* (he/she), *-bant* (they)\\n"
                "**Future**: *-bit* (he/she), *-bunt* (they)\\n"
                "**Perfect**: *-vit* (he/she), *-verunt* (they)\\n"
                "**Pluperfect**: *-verat* (he/she), *-verant* (they)"),
        "pass_mark":80,
        "content":{"questions":TENSE_ID_QUESTIONS},
    },
    {
        "id":17, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Parsing Forms",
        "type":"parsing",
        "sell":"Identify the tense, person and number of each form. Click the correct button for each, then press Check.",
        "pass_mark":80,
        "content":{"questions":PARSING_QUESTIONS},
    },
    {
        "id":18, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Translating Forms",
        "type":"parsing_mcq",
        "sell":"Translate the inflected form. Four options - always in the same order.",
        "pass_mark":80,
        "content":{"questions":MCQ_QUESTIONS},
    },
    {
        "id":19, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Mixed Sentences",
        "type":"sentences",
        "sell":"Translate these sentences into English. All verbs are 1st conjugation. All vocabulary is from the Top 150.",
        "pass_mark":80,
        "content":{"sentences":NODE1_SENTENCES},
    },
]"""

# Replace the entire SETS array
pattern = r'SETS = \[(.*?)\]\n\nSETS_BY_ID'
match = re.search(pattern, text, re.DOTALL)
if match:
    text = text[:match.start()] + new_sets_str + "\n\nSETS_BY_ID" + text[match.end():]
else:
    print("Could not find SETS array to replace")

with open('data.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated data.py SETS structure!")
