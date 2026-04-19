import json

# Sentences 
SENT_PRES = """

# Set 8: Sentences: Present Tense
SENTENCES_PRESENT_TEST = [
    {
        "latin": "puella laeta clamat.",
        "english": ["the happy girl shouts", "a happy girl shouts", "the happy girl is shouting"],
        "explanation": "**puella laeta** = the happy girl. **clamat** = she shouts (present)."
    },
    {
        "latin": "regina irata oppugnat.",
        "english": ["the angry queen attacks", "an angry queen attacks", "the angry queen is attacking"],
        "explanation": "**regina irata** = the angry queen. **oppugnat** = she attacks (present)."
    },
    {
        "latin": "miles per silvam festinat.",
        "english": ["the soldier hurries through the wood", "a soldier hurries through the wood", "the soldier is hurrying through the wood"],
        "explanation": "**miles** = the soldier. **per silvam** = through the wood. **festinat** = he hurries (present)."
    },
    {
        "latin": "femina deos orat.",
        "english": ["the woman begs the gods", "a woman begs the gods", "the woman is begging the gods"],
        "explanation": "**femina** = the woman. **deos** = the gods (accusative plural). **orat** = she begs (present)."
    }
]

"""

SENT_PRES_SYS = """

# Set 12: Sentences: The Present System (Present, Imperfect, Future, Infinitives)
SENTENCES_PRESENT_SYSTEM = [
    {
        "latin": "regina necare imperabat.",
        "english": ["the queen was ordering to kill", "a queen was ordering to kill"],
        "explanation": "**regina** = the queen. **necare** = to kill (infinitive). **imperabat** = she was ordering (imperfect)."
    },
    {
        "latin": "puellae fessae clamabant.",
        "english": ["the tired girls were shouting", "tired girls were shouting"],
        "explanation": "**puellae fessae** = the tired girls. **clamabant** = they were shouting (imperfect plural)."  # wait, fessus not in list. I will use 'laetae'
    },
    {
        "latin": "puellae laetae clamabant.",
        "english": ["the happy girls were shouting", "happy girls were shouting", "the happy girls used to shout"],
        "explanation": "**puellae laetae** = the happy girls. **clamabant** = they were shouting (imperfect plural). The imperfect describes ongoing action in the past."
    },
    {
        "latin": "femina in oppido habitabit.",
        "english": ["the woman will live in the town", "a woman will live in the town"],
        "explanation": "**femina** = the woman. **in oppido** = in the town. **habitabit** = she will live (future)."  # wait, oppidum not in list. I will use 'insula' or 'urbs'. 'urbs'
    },
    {
        "latin": "femina in urbe habitabit.",
        "english": ["the woman will live in the city", "a woman will live in the city"],
        "explanation": "**femina** = the woman. **in urbe** = in the city. **habitabit** = she will live (future). Note the -bi- tense marker for the future."
    },
    {
        "latin": "regem rogabo.",
        "english": ["I will ask the king", "I shall ask the king"],
        "explanation": "**regem** = the king (accusative). **rogabo** = I will ask (future)."
    }
]
# Clean it up by removing the invalid ones:
SENTENCES_PRESENT_SYSTEM = [
    {
        "latin": "regina necare imperabat.",
        "english": ["the queen was ordering to kill", "a queen was ordering to kill", "the queen used to order to kill"],
        "explanation": "**regina** = the queen. **necare** = to kill (infinitive). **imperabat** = she was ordering (imperfect)."
    },
    {
        "latin": "puellae laetae clamabant.",
        "english": ["the happy girls were shouting", "happy girls were shouting", "the happy girls used to shout"],
        "explanation": "**puellae laetae** = the happy girls. **clamabant** = they were shouting (imperfect plural). The imperfect describes ongoing action in the past."
    },
    {
        "latin": "femina in urbe habitabit.",
        "english": ["the woman will live in the city", "a woman will live in the city"],
        "explanation": "**femina** = the woman. **in urbe** = in the city. **habitabit** = she will live (future). Note the -bi- tense marker for the future."
    },
    {
        "latin": "regem rogabo.",
        "english": ["I will ask the king", "I shall ask the king"],
        "explanation": "**regem** = the king (accusative). **rogabo** = I will ask (future)."
    }
]

"""

SENT_ACTIVE = """

# Set 18: Sentences: All Active Tenses
SENTENCES_ACTIVE = [
    {
        "latin": "regina irata oppugnavit.",
        "english": ["the angry queen attacked", "an angry queen attacked", "the angry queen has attacked"],
        "explanation": "**regina irata** = the angry queen. **oppugnavit** = she attacked (perfect)."
    },
    {
        "latin": "miles per silvam festinaverat.",
        "english": ["the soldier had hurried through the wood", "a soldier had hurried through the wood"],
        "explanation": "**miles** = the soldier. **festinaverat** = he had hurried (pluperfect). The pluperfect describes action completed further back in the past."
    },
    {
        "latin": "femina laeta oraverat.",
        "english": ["the happy woman had begged", "a happy woman had begged"],
        "explanation": "**femina laeta** = the happy woman. **oraverat** = she had begged (pluperfect)."
    },
    {
        "latin": "rex militibus imperavit.",
        "english": ["the king ordered the soldiers", "a king ordered the soldiers", "the king gave orders to the soldiers"],
        "explanation": "**rex** = the king. **militibus** = to the soldiers (dative). **imperavit** = he ordered (perfect)."
    }
]

"""

SENT_PPP = """

# Set 20: Sentences: PPPs
SENTENCES_PPP = [
    {
        "latin": "puella liberata laeta erat.",
        "english": ["the freed girl was happy", "the girl having been freed was happy", "a freed girl was happy"],
        "explanation": "**puella liberata** = the freed girl. **laeta erat** = she was happy."
    },
    {
        "latin": "rex oppugnatus milites rogavit.",
        "english": ["the attacked king asked the soldiers", "the king having been attacked asked the soldiers"],
        "explanation": "**rex oppugnatus** = the attacked king. **milites** = the soldiers (accusative object). **rogavit** = he asked (perfect)."
    },
    {
        "latin": "feminae perterritae deos oraverunt.",
        "english": ["the terrified women begged the gods", "terrified women begged the gods", "the terrified women prayed to the gods"],
        "explanation": "**feminae perterritae** = the terrified women. **deos** = the gods. **oraverunt** = they begged (perfect)."
    }
]

"""

SETS_DEF = r'''
# ── SETS ──────────────────────────────────────────────────────────────────────
SETS = [
    # -- Node 0: Introduction --------------------------------------------------
    {
        "id":1, "node":0, "node_title":"Introduction",
        "title":"What is a verb?",
        "type":"reference", "optional":True,
        "sell":"Before starting, make sure you know exactly what a verb is and how they work in English.\\n\\nA verb is a **doing word**. It usually describes an action (like *run*, *laugh*, or *attack*), but can also describe a state of being (like *is*, *was*, *seems*).\n\nEvery sentence needs a verb to make sense. Without one, you just have a collection of things doing nothing.",
    },
    {
        "id":2, "node":0, "node_title":"Introduction",
        "title":"Verbs vs Nouns",
        "type":"concept",
        "sell":"Test your understanding! Read the English sentences below and identify the verb.",
        "pass_mark":100,
        "content":{"questions":VERB_IDENTIFY}
    },
    {
        "id":3, "node":0, "node_title":"Introduction",
        "title":"The Four Principal Parts",
        "type":"reference", "optional":True,
        "sell":"To master a Latin verb, you must learn its **four Principal Parts**.\\n\\nUnlike nouns which have a single dictionary form, Latin verbs change their shape so radically depending on their tense (past/present/future) that dictionaries list four different 'base' forms for each verb to help you build any tense you need.\\n\\nFor example, to look up 'love', the dictionary will give you:\\n\\n**amo, amare, amavi, amatus**\\n\\nYou will learn what each of these blocks do in the next nodes. For now, just understand that these four parts are the vital building blocks of every verb.",
    },
    {
        "id":4, "node":0, "node_title":"Introduction",
        "title":"Conjugations",
        "type":"reference", "optional":True,
        "sell":"Verbs in Latin belong to families called **Conjugations**. There are four main conjugations, just like Hogwarts houses.\\n\\nVerbs in the same conjugation share the same vowels and follow the exact same rules. If you know how one 1st Conjugation verb behaves, you know how they almost all behave!\\n\\nIn this curriculum, we will learn them conjugation by conjugation, starting with the 1st.",
    },

    # -- Node 1: 1st Conjugation -----------------------------------------------
    {
        "id":5, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Key Vocabulary",
        "type":"vocab", "optional":True,
        "sell":"These are the core nouns, adjectives and prepositions that accompany the verbs in this section. Reviewing them is highly recommended.",
        "pass_mark":80,
        "content":{"vocab":NODE1_VOCAB, "mode":"meanings"},
    },
    {
        "id":6, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"1st Principal Part",
        "type":"verbs",
        "sell":"The 13 most frequent 1st conjugation verbs. Learn what each one means.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The First Principal Part",
                "body":"The **1st principal part** is the form you look up in a dictionary. It's the 1st person singular present tense — meaning **I ...**\\n\\nFor 1st conjugation verbs it always ends in **-o**:\\n\\n*amo* = I love\\n*clamo* = I shout\\n*rogo* = I ask\\n\\nWhen you see a Latin word ending in **-o**, that's your clue it's the 1st person present.",
            }
        ],
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"meanings"},
    },
    {
        "id":7, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Present Tense Endings",
        "type":"translate_form",
        "sell":"The present tense endings indicate who is doing the action. Let's practice differentiating them.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"1st Conjugation: Present Tense Endings",
                "body":"Take the present stem (amo -> ama-) and add the endings:",
                "table":[
                    {"conjugation":"1st person singular (I)","infinitive_ending":"o","example":"amo (I love)"},
                    {"conjugation":"2nd person singular (you sg)","infinitive_ending":"s","example":"amas (you love)"},
                    {"conjugation":"3rd person singular (he/she/it)","infinitive_ending":"t","example":"amat (he/she loves)"},
                    {"conjugation":"1st person plural (we)","infinitive_ending":"mus","example":"amamus (we love)"},
                    {"conjugation":"2nd person plural (you pl)","infinitive_ending":"tis","example":"amatis (you love)"},
                    {"conjugation":"3rd person plural (they)","infinitive_ending":"nt","example":"amant (they love)"}
                ],
                "table_note":"You will now practice identifying these endings.",
                "infinitive_ending_header":"Personal ending"
            }
        ],
        "content":{"questions":QUESTIONS_PRESENT}
    },
    {
        "id":8, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: Present",
        "type":"sentences",
        "sell":"Translate these sentences into English. All verbs are in the present tense.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_TEST},
    },
    {
        "id":9, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Infinitive",
        "type":"building_parts",
        "sell":"Learn the 2nd principal part: the Infinitive. You will type it out for all incoming verbs.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"infinitives",
            "show_parts_so_far":1,
            "pattern_screen":{"title":"1st Conjugation: The Infinitive","subtitle":"Add -re to the present stem:","examples":[{"stem":"ama","inf":"amare","english":"to love","present":"amo"},{"stem":"roga","inf":"rogare","english":"to ask","present":"rogo"},{"stem":"clama","inf":"clamare","english":"to shout","present":"clamo"}]}
        },
    },
    {
        "id":10, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Imperfect Tense",
        "type":"translate_form",
        "sell":"The imperfect tense describes continuous or repeated past action.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Imperfect Tense",
                "body":"Built on the present stem, the imperfect adds the marker **-ba-** before the personal endings:",
                "table":[
                    {"conjugation":"1st singular (I)","infinitive_ending":"bam","example":"amabam (I was loving)"},
                    {"conjugation":"2nd singular (you)","infinitive_ending":"bas","example":"amabas (you were loving)"},
                    {"conjugation":"3rd singular (he/she/it)","infinitive_ending":"bat","example":"amabat (he/she was loving)"},
                    {"conjugation":"1st plural (we)","infinitive_ending":"bamus","example":"amabamus (we were loving)"},
                    {"conjugation":"2nd plural (you pl)","infinitive_ending":"batis","example":"amabatis (you were loving)"},
                    {"conjugation":"3rd plural (they)","infinitive_ending":"bant","example":"amabant (they were loving)"}
                ],
                "table_note":"Try to spot the 'ba' marker immediately to recognise the imperfect.",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_IMPERFECT}
    },
    {
        "id":11, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Future Tense",
        "type":"translate_form",
        "sell":"The future tense describes events yet to happen.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Future Tense",
                "body":"Also built on the present stem using a completely different marker (**-bi-** and **-bo-**). Do not confuse it with the imperfect!",
                "table":[
                    {"conjugation":"1st singular (I)","infinitive_ending":"bo","example":"amabo (I will love)"},
                    {"conjugation":"2nd singular (you)","infinitive_ending":"bis","example":"amabis (you will love)"},
                    {"conjugation":"3rd singular (he/she/it)","infinitive_ending":"bit","example":"amabit (he/she will love)"},
                    {"conjugation":"1st plural (we)","infinitive_ending":"bimus","example":"amabimus (we will love)"},
                    {"conjugation":"2nd plural (you pl)","infinitive_ending":"bitis","example":"amabitis (you will love)"},
                    {"conjugation":"3rd plural (they)","infinitive_ending":"bunt","example":"amabunt (they will love)"}
                ],
                "table_note":"Watch out for the difference between -bat (imperfect) and -bit (future)!",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_FUTURE}
    },
    {
        "id":12, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: The Present System",
        "type":"sentences",
        "sell":"Translate these sentences covering everything built off the present stem (Present, Imperfect, Future, Infinitives).",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PRESENT_SYSTEM},
    },
    {
        "id":13, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"3rd Principal Part",
        "type":"building_parts",
        "sell":"We move to the perfect stem. Learn the 3rd principal part: the 1st Person Perfect Tense.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"perfects",  # shows all 3
            "show_parts_so_far":2,
            "pattern_screen":{"title":"1st Conjugation: Perfect","subtitle":"Take the infinitive, remove the -re, add -vi:","examples":[{"full":"amavi","ending":"vi","inf":"amare","english":"I loved"},{"full":"rogavi","ending":"vi","inf":"rogare","english":"I asked"},{"full":"necavi","ending":"vi","inf":"necare","english":"I killed"},{"full":"navigavi","ending":"vi","inf":"navigare","english":"I sailed"},{"full":"festinavi","ending":"vi","inf":"festinare","english":"I hurried"}],"footnote":"The **-v-** is the past marker. Look for the -v- to spot a perfect tense form."}
        },
    },
    {
        "id":14, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Perfect Tense Endings",
        "type":"translate_form",
        "sell":"Learn exactly how the perfect tense works for the remaining 5 persons.",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Perfect Tense",
                "body":"Built on the 3rd principal part (perfect stem). Used for actions completed in the past.",
                "table":[
                    {"conjugation":"1st singular (I)","infinitive_ending":"i","example":"amavi (I loved)"},
                    {"conjugation":"2nd singular (you)","infinitive_ending":"isti","example":"amavisti (you loved)"},
                    {"conjugation":"3rd singular (he/she/it)","infinitive_ending":"it","example":"amavit (he/she loved)"},
                    {"conjugation":"1st plural (we)","infinitive_ending":"imus","example":"amavimus (we loved)"},
                    {"conjugation":"2nd plural (you pl)","infinitive_ending":"istis","example":"amavistis (you loved)"},
                    {"conjugation":"3rd plural (they)","infinitive_ending":"erunt","example":"amaverunt (they loved)"}
                ],
                "table_note":"Watch for the telltale -v- in 1st conjugation perfects.",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_PERFECT}
    },
    {
        "id":15, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"The Pluperfect Tense",
        "type":"translate_form",
        "sell":"Learn the pluperfect: actions completed even further back in the past ('had done').",
        "pass_mark":80,
        "screens":[
            {
                "heading":"The Pluperfect Tense",
                "body":"Also built on the perfect stem. The endings look like the imperfect tense of 'sum'.",
                "table":[
                    {"conjugation":"1st singular (I)","infinitive_ending":"eram","example":"amaveram (I had loved)"},
                    {"conjugation":"2nd singular (you)","infinitive_ending":"eras","example":"amaveras (you had loved)"},
                    {"conjugation":"3rd singular (he/she/it)","infinitive_ending":"erat","example":"amaverat (he/she had loved)"},
                    {"conjugation":"1st plural (we)","infinitive_ending":"eramus","example":"amaveramus (we had loved)"},
                    {"conjugation":"2nd plural (you pl)","infinitive_ending":"eratis","example":"amaveratis (you had loved)"},
                    {"conjugation":"3rd plural (they)","infinitive_ending":"erant","example":"amaverant (they had loved)"}
                ],
                "table_note":"Spot the combination of the -v- marker and the -era- marker: am-av-era-m.",
                "infinitive_ending_header":"Ending"
            }
        ],
        "content":{"questions":QUESTIONS_PLUPERFECT}
    },
    {
        "id":16, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: All Active Tenses",
        "type":"sentences",
        "sell":"The grand culmination. Translate these sentences mixing any active tense learnt so far.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_ACTIVE},
    },
    {
        "id":17, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"4th Principal Part (PPP)",
        "type":"building_parts",
        "sell":"The final principal part. The Perfect Passive Participle.",
        "pass_mark":80,
        "content":{
            "verbs":VERBS_1ST_TOP150,
            "mode":"ppps",
            "show_parts_so_far":3,
            "pattern_screen":{"title":"1st Conjugation: PPPs","subtitle":"The PPP translates as 'having been...' and acts like an adjective. Take the dictionary form, drop the -o, add -atus:","examples":[{"full":"amatus (-a, -um)","ending":"atus","inf":"amavi","present":"amo","english":"having been loved"},{"full":"rogatus (-a,-um)","ending":"atus","inf":"rogavi","present":"rogo","english":"having been asked"},{"full":"necatus (-a,-um)","ending":"atus","inf":"necavi","present":"neco","english":"having been killed"}]}
        },
    },
    {
        "id":18, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Sentences: PPPs",
        "type":"sentences",
        "sell":"Translate these sentences and correctly translate the PPPs in context.",
        "pass_mark":80,
        "content":{"sentences":SENTENCES_PPP},
    },
    {
        "id":19, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"Fill the Missing Part",
        "type":"building_parts",
        "sell":"You will see three Principal Parts. Type the missing part in the blank.",
        "pass_mark":80,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"all_four", "show_parts_so_far":4, "gap_positions":[1, 2, 3]},
    },
    {
        "id":20, "node":1, "node_title":"1st Conjugation (Top 150)",
        "title":"All Four Parts",
        "type":"building_parts",
        "sell":"The ultimate test. Type the 3 missing parts in order.",
        "pass_mark":100,
        "content":{"verbs":VERBS_1ST_TOP150, "mode":"all_four_from_present", "show_parts_so_far":4, "gap_positions":[1,2,3]},
    },
]
'''

import sys
with open('data.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("SETS = [")
if idx == -1:
    print("Failed to find SETS = [")
    sys.exit(1)

# Find the exact header to keep it clean
header_idx = text.rfind("# ── SETS ──", 0, idx)
if header_idx != -1:
    idx = header_idx

prefix = text[:idx]

with open('generated_sets.txt', 'r', encoding='utf-8') as f:
    gen_text = f.read()

new_content = prefix + "\n\n" + gen_text + SENT_PRES + SENT_PRES_SYS + SENT_ACTIVE + SENT_PPP + SETS_DEF

with open('data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done building curriculum!")
