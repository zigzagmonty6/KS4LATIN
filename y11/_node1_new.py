# Node 1 rewrite — generated from CURRICULUM_SENTENCES.docx
# Teacher-approved format:
#   - Ideal = strict literal; alternatives = natural / alternate glosses
#   - PPPs: ideal = "having been X-ed"
#   - Imperfect: ideal = "was X-ing", alts add "used to" / simple past / "kept X-ing"
#   - Perfect: ideal = "X-ed", alts add "has X-ed" / "did X"
#   - Present: ideal = "X-s", alts add "is X-ing"
#   - Verb-person: say "he/she" form, NOT "3rd singular"
#   - "tum" = only "then"
#   - Explanation bullets: per-word/phrase, case + number for nouns, tense + person (as "he/she") + number for verbs
#   - Sentence #27 in Set 12 REWRITTEN: "tam" and "erat" removed (pre-Node-5)
#     original:  illa dea ad feminam appropinquavit, nam tam tristis erat.
#     rewrite:   illa dea ad tristem feminam appropinquavit, et clamabat.
#     confirm this with teacher on review

# ════════════════════════════════════════════════════════════════════════════
# NODE1_VOCAB — sliced into preview groups aligned to each sentence set
# ════════════════════════════════════════════════════════════════════════════

NODE1_VOCAB_SET4_PREVIEW = [
    # Verbs (1st conjugation, introduced here)
    {"id":"amo",         "latin":"amo",         "english":["I love"],       "pos":"verb"},
    {"id":"rogo",        "latin":"rogo",        "english":["I ask"],        "pos":"verb"},
    {"id":"habito",      "latin":"habito",      "english":["I live"],       "pos":"verb"},
    {"id":"navigo",      "latin":"navigo",      "english":["I sail"],       "pos":"verb"},
    {"id":"clamo",       "latin":"clamo",       "english":["I shout"],      "pos":"verb"},
    {"id":"appropinquo", "latin":"appropinquo", "english":["I approach"],   "pos":"verb"},
    {"id":"impero",      "latin":"impero",      "english":["I order"],      "pos":"verb", "notes":"+ dative"},
    {"id":"festino",     "latin":"festino",     "english":["I hurry"],      "pos":"verb"},
    {"id":"oro",         "latin":"oro",         "english":["I beg"],        "pos":"verb"},
    {"id":"oppugno",     "latin":"oppugno",     "english":["I attack"],     "pos":"verb"},
    {"id":"libero",      "latin":"libero",      "english":["I free"],       "pos":"verb"},
    {"id":"neco",        "latin":"neco",        "english":["I kill"],       "pos":"verb"},
    # Nouns
    {"id":"puella",  "latin":"puella",  "english":["girl"],      "pos":"noun"},
    {"id":"dea",     "latin":"dea",     "english":["goddess"],   "pos":"noun"},
    {"id":"femina",  "latin":"femina",  "english":["woman"],     "pos":"noun"},
    {"id":"pater",   "latin":"pater",   "english":["father"],    "pos":"noun"},
    {"id":"filia",   "latin":"filia",   "english":["daughter"],  "pos":"noun"},
    {"id":"insula",  "latin":"insula",  "english":["island"],    "pos":"noun"},
    {"id":"regina",  "latin":"regina",  "english":["queen"],     "pos":"noun"},
    {"id":"deus",    "latin":"deus",    "english":["god"],       "pos":"noun"},
    {"id":"terra",   "latin":"terra",   "english":["land", "earth", "ground"], "pos":"noun"},
    {"id":"urbs",    "latin":"urbs",    "english":["city"],      "pos":"noun"},
    # Adjectives
    {"id":"pulcher", "latin":"pulcher", "english":["beautiful"], "pos":"adjective"},
    {"id":"tristis", "latin":"tristis", "english":["sad"],       "pos":"adjective"},
    {"id":"laetus",  "latin":"laetus",  "english":["happy"],     "pos":"adjective"},
    {"id":"ingens",  "latin":"ingens",  "english":["huge"],      "pos":"adjective"},
    # Pronouns
    {"id":"ego",     "latin":"ego",     "english":["I"],         "pos":"pronoun"},
    # Prepositions
    {"id":"in_acc",  "latin":"in",      "english":["into", "onto"], "pos":"preposition", "display_label":"+ acc"},
    {"id":"in_abl",  "latin":"in",      "english":["in", "on"],     "pos":"preposition", "display_label":"+ abl"},
    {"id":"ad",      "latin":"ad",      "english":["to", "towards"],"pos":"preposition"},
    {"id":"per",     "latin":"per",     "english":["through"],   "pos":"preposition"},
    # Conjunctions / adverbs
    {"id":"et",      "latin":"et",      "english":["and"],       "pos":"conjunction"},
    {"id":"sed",     "latin":"sed",     "english":["but"],       "pos":"conjunction"},
    {"id":"nam",     "latin":"nam",     "english":["for"],       "pos":"conjunction"},
    {"id":"non",     "latin":"non",     "english":["not"],       "pos":"adverb"},
    {"id":"ibi",     "latin":"ibi",     "english":["there"],     "pos":"adverb"},
    {"id":"multus",  "latin":"multus",  "english":["many", "much"], "pos":"adjective"},
]

NODE1_VOCAB_SET8_PREVIEW = [
    {"id":"puto",    "latin":"puto",    "english":["I think"],   "pos":"verb", "notes":"+ double accusative"},
    {"id":"ille",    "latin":"ille, illa, illud", "english":["that", "he", "she", "it"], "pos":"demonstrative"},
    {"id":"tum",     "latin":"tum",     "english":["then"],      "pos":"adverb"},
    {"id":"subito",  "latin":"subito",  "english":["suddenly"],  "pos":"adverb"},
    {"id":"me",      "latin":"me",      "english":["me"],        "pos":"pronoun", "display_label":"acc"},
]

NODE1_VOCAB_SET12_PREVIEW = [
    {"id":"domum",   "latin":"domum",   "english":["home", "homewards"], "pos":"noun", "notes":"accusative of motion"},
    {"id":"mihi",    "latin":"mihi",    "english":["to me", "for me"],   "pos":"pronoun", "display_label":"dat"},
    {"id":"prope",   "latin":"prope",   "english":["near"],      "pos":"preposition"},
    {"id":"etiam",   "latin":"etiam",   "english":["even", "also", "still"], "pos":"adverb"},
]

NODE1_VOCAB_SET14_PREVIEW = [
    # No new lemmas — this is the PPP form-drill. PPP stems of known verbs:
    # amatus, liberatus, necatus, oppugnatus, oratus, imperatus, rogatus
    # The preview here is a form-recognition drill, not new cards.
]

NODE1_VOCAB_SET16_PREVIEW = [
    {"id":"que",     "latin":"-que",    "english":["and"],       "pos":"conjunction", "notes":"attached as suffix"},
    {"id":"illud",   "latin":"illud",   "english":["that (thing)"], "pos":"demonstrative", "display_label":"neut sg"},
]

# Full Node 1 vocabulary (assembled in pedagogical order)
NODE1_VOCAB = (
    NODE1_VOCAB_SET4_PREVIEW
    + NODE1_VOCAB_SET8_PREVIEW
    + NODE1_VOCAB_SET12_PREVIEW
    + NODE1_VOCAB_SET16_PREVIEW
)

# ════════════════════════════════════════════════════════════════════════════
# SENTENCES — Node 1
# ════════════════════════════════════════════════════════════════════════════

# Set 4 — Present tense
SENTENCES_N1_SET4 = [
    {
        "latin": "puella deam amat.",
        "english": [
            "The girl loves the goddess.",
            "The girl is loving the goddess.",
            "The girl likes the goddess.",
            "A girl loves a goddess.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject\n"
            "• deam (goddess) — accusative singular, direct object\n"
            "• amat (loves) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "pater filiam rogat.",
        "english": [
            "The father asks the daughter.",
            "The father asks his daughter.",
            "The father questions the daughter.",
            "The father is asking the daughter.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject\n"
            "• filiam (daughter) — accusative singular, direct object\n"
            "• rogat (asks) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "femina in insula habitat.",
        "english": [
            "The woman lives on the island.",
            "The woman is living on the island.",
            "The woman lives in the island.",
            "A woman lives on an island.",
        ],
        "explanation": (
            "• femina (woman) — nominative singular, subject\n"
            "• in insula (on the island) — prepositional phrase: in + ablative = in/on\n"
            "• habitat (lives) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "dea pulchra ad terram navigat.",
        "english": [
            "The beautiful goddess sails towards the land.",
            "The beautiful goddess sails to the land.",
            "The beautiful goddess is sailing towards the land.",
            "A beautiful goddess sails towards the country.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject\n"
            "• pulchra (beautiful) — adjective, nominative singular feminine, agreeing with dea\n"
            "• ad terram (towards the land) — prepositional phrase: ad + accusative = to/towards\n"
            "• navigat (sails) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "regina tristis clamat, nam deus appropinquat.",
        "english": [
            "The sad queen shouts, for the god approaches.",
            "The sad queen is shouting, for the god is approaching.",
            "The unhappy queen shouts, because the god approaches.",
            "The sad queen shouts, for the god draws near.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject of first clause\n"
            "• tristis (sad) — adjective, nominative singular, agreeing with regina\n"
            "• clamat (shouts) — verb, present tense, he/she form\n"
            "• nam (for) — conjunction introducing a reason\n"
            "• deus (god) — nominative singular, subject of second clause\n"
            "• appropinquat (approaches) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "puella laeta patri imperat, et pater festinat.",
        "english": [
            "The happy girl orders the father, and the father hurries.",
            "The happy girl orders her father, and the father hurries.",
            "The joyful girl orders the father, and the father rushes.",
            "The happy girl is ordering the father, and the father is hurrying.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• laeta (happy) — adjective, nominative singular feminine, agreeing with puella\n"
            "• patri (father) — DATIVE singular (impero takes the dative — not 'to the father')\n"
            "• imperat (orders) — verb, present tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• festinat (hurries) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "ego feminam oro, sed dea non clamat.",
        "english": [
            "I beg the woman, but the goddess does not shout.",
            "I beg the woman, but the goddess is not shouting.",
            "I myself beg the woman, but the goddess does not shout.",
            "I plead with the woman, but the goddess does not shout.",
        ],
        "explanation": (
            "• ego (I) — nominative singular, emphatic subject of first clause\n"
            "• feminam (woman) — accusative singular, direct object\n"
            "• oro (I beg) — verb, present tense, I form\n"
            "• sed (but) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• non (not) — negates the verb\n"
            "• clamat (shouts) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "multi dei insulam oppugnant, et ibi feminae clamant.",
        "english": [
            "Many gods attack the island, and there the women shout.",
            "Many gods are attacking the island, and there the women are shouting.",
            "Many of the gods attack the island, and the women are shouting there.",
            "Many gods attack the island, and the women shout there.",
        ],
        "explanation": (
            "• multi (many) — adjective, nominative plural masculine, agreeing with dei\n"
            "• dei (gods) — nominative plural, subject of first clause\n"
            "• insulam (island) — accusative singular, direct object\n"
            "• oppugnant (attack) — verb, present tense, they form\n"
            "• et (and) — coordinating conjunction\n"
            "• ibi (there) — adverb, flexible position in English\n"
            "• feminae (women) — nominative plural, subject of second clause\n"
            "• clamant (shout) — verb, present tense, they form"
        ),
    },
    {
        "latin": "deus ingens per urbem festinat, et regina puellas liberat.",
        "english": [
            "The huge god hurries through the city, and the queen frees the girls.",
            "The enormous god hurries through the city, and the queen sets free the girls.",
            "The huge god rushes through the city, and the queen frees the girls.",
            "The vast god is hurrying through the city, and the queen is freeing the girls.",
        ],
        "explanation": (
            "• deus (god) — nominative singular, subject of first clause\n"
            "• ingens (huge) — adjective, nominative singular, agreeing with deus\n"
            "• per urbem (through the city) — prepositional phrase: per + accusative\n"
            "• festinat (hurries) — verb, present tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• regina (queen) — nominative singular, subject of second clause\n"
            "• puellas (girls) — accusative plural, direct object\n"
            "• liberat (frees) — verb, present tense, he/she form"
        ),
    },
    {
        "latin": "pater puellam necat, et dea tristis deos orat.",
        "english": [
            "The father kills the girl, and the sad goddess begs the gods.",
            "The father kills the girl, and the unhappy goddess begs the gods.",
            "The father murders the girl, and the sad goddess pleads with the gods.",
            "The father is killing the girl, and the sad goddess is praying to the gods.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject of first clause\n"
            "• puellam (girl) — accusative singular, direct object\n"
            "• necat (kills) — verb, present tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• tristis (sad) — adjective agreeing with dea\n"
            "• deos (gods) — accusative plural, direct object\n"
            "• orat (begs) — verb, present tense, he/she form"
        ),
    },
]

# Set 8 — Imperfect & Future
SENTENCES_N1_SET8 = [
    {
        "latin": "dea clamabat.",
        "english": [
            "The goddess was shouting.",
            "The goddess used to shout.",
            "The goddess kept shouting.",
            "The goddess shouted.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject\n"
            "• clamabat (was shouting) — verb, imperfect tense (the -ba- marker), he/she form"
        ),
    },
    {
        "latin": "pater navigabit.",
        "english": [
            "The father will sail.",
            "The father will be sailing.",
            "The father is going to sail.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject\n"
            "• navigabit (will sail) — verb, future tense (the -bi- marker), he/she form"
        ),
    },
    {
        "latin": "puella tum clamabat, et pater navigabat.",
        "english": [
            "The girl was then shouting, and the father was sailing.",
            "Then the girl was shouting, and the father was sailing.",
            "The girl then used to shout, and the father used to sail.",
            "The girl was shouting then, and the father was sailing.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• tum (then) — adverb (flexible position in English)\n"
            "• clamabat (was shouting) — verb, imperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• navigabat (was sailing) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "regina feminam rogabit, et femina deam orabit.",
        "english": [
            "The queen will ask the woman, and the woman will beg the goddess.",
            "The queen is going to ask the woman, and the woman is going to beg the goddess.",
            "The queen will question the woman, and the woman will pray to the goddess.",
            "The queen will be asking the woman, and the woman will be begging the goddess.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject of first clause\n"
            "• feminam (woman) — accusative singular, direct object\n"
            "• rogabit (will ask) — verb, future tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• femina (woman) — nominative singular, subject of second clause\n"
            "• deam (goddess) — accusative singular, direct object\n"
            "• orabit (will beg) — verb, future tense, he/she form"
        ),
    },
    {
        "latin": "multi dei subito urbem oppugnabant, sed regina in insula habitabat.",
        "english": [
            "Many gods were suddenly attacking the city, but the queen was living on the island.",
            "Suddenly many gods were attacking the city, but the queen used to live on the island.",
            "Many gods suddenly used to attack the city, but the queen was living on the island.",
            "Many gods were suddenly attacking the city, but the queen lived in the island.",
        ],
        "explanation": (
            "• multi (many) — adjective agreeing with dei\n"
            "• dei (gods) — nominative plural, subject of first clause\n"
            "• subito (suddenly) — adverb (flexible position)\n"
            "• urbem (city) — accusative singular, direct object\n"
            "• oppugnabant (were attacking) — verb, imperfect tense, they form\n"
            "• sed (but) — coordinating conjunction\n"
            "• regina (queen) — nominative singular, subject of second clause\n"
            "• in insula (on the island) — prepositional phrase: in + ablative\n"
            "• habitabat (was living) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "puella pulchra in urbem festinabit, et pater clamabit.",
        "english": [
            "The beautiful girl will hurry into the city, and the father will shout.",
            "The beautiful girl will rush into the city, and the father will shout.",
            "The beautiful girl will be hurrying to the city, and the father will be shouting.",
            "The beautiful girl will hurry to the city, and the father will shout.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• pulchra (beautiful) — adjective agreeing with puella\n"
            "• in urbem (into the city) — prepositional phrase: in + accusative = into\n"
            "• festinabit (will hurry) — verb, future tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• clamabit (will shout) — verb, future tense, he/she form"
        ),
    },
    {
        "latin": "dea me amabat, sed pater tum non orabat.",
        "english": [
            "The goddess was loving me, but the father was not then begging.",
            "The goddess used to love me, but the father was not begging then.",
            "The goddess loved me, but the father did not beg then.",
            "The goddess was loving me, but my father was not begging then.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject of first clause\n"
            "• me (me) — accusative singular pronoun, direct object\n"
            "• amabat (was loving) — verb, imperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• tum (then) — adverb (flexible position)\n"
            "• non (not) — negates the verb\n"
            "• orabat (was begging) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "dea patrem liberabit, et pater deae tum imperabit.",
        "english": [
            "The goddess will free the father, and the father will then order the goddess.",
            "The goddess will set free the father, and then the father will order the goddess.",
            "The goddess will free the father, and the father will then order the goddess.",
            "The goddess will free her father, and the father will then order the goddess.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject of first clause\n"
            "• patrem (father) — accusative singular, direct object\n"
            "• liberabit (will free) — verb, future tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• deae (goddess) — DATIVE singular (impero takes the dative — not 'to the goddess')\n"
            "• tum (then) — adverb (flexible position)\n"
            "• imperabit (will order) — verb, future tense, he/she form"
        ),
    },
    {
        "latin": "regina illa deum laetum putabat, sed dea non orabat.",
        "english": [
            "That queen was thinking the god happy, but the goddess was not begging.",
            "That queen thought the god happy, but the goddess was not begging.",
            "That queen used to think the god happy, but the goddess did not beg.",
            "That queen considered the god happy, but the goddess was not praying.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject of first clause\n"
            "• illa (that) — demonstrative agreeing with regina\n"
            "• deum (god) — accusative singular, direct object\n"
            "• laetum (happy) — adjective agreeing with deum — this is the 'double accusative' with puto: 'think X (to be) Y'\n"
            "• putabat (was thinking) — verb, imperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, new subject\n"
            "• non (not) — negates the verb\n"
            "• orabat (was begging) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "ingens navis per terram navigabat, et puella pulchra clamabat.",
        "english": [
            "A huge ship was sailing through the land, and the beautiful girl was shouting.",
            "An enormous ship was sailing through the land, and the beautiful girl was shouting.",
            "A huge ship used to sail through the land, and the beautiful girl kept shouting.",
            "A huge ship was sailing through the country, and the beautiful girl was shouting.",
        ],
        "explanation": (
            "• ingens (huge) — adjective, nominative singular, agreeing with navis\n"
            "• navis (ship) — nominative singular, subject of first clause\n"
            "• per terram (through the land) — prepositional phrase: per + accusative\n"
            "• navigabat (was sailing) — verb, imperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• puella (girl) — nominative singular, subject of second clause\n"
            "• pulchra (beautiful) — adjective agreeing with puella\n"
            "• clamabat (was shouting) — verb, imperfect tense, he/she form"
        ),
    },
]

# Set 12 — Perfect & Pluperfect
# NOTE: sentence #27 rewritten to remove 'tam' and 'erat' (both belong to Node 5)
SENTENCES_N1_SET12 = [
    {
        "latin": "puella clamavit.",
        "english": [
            "The girl shouted.",
            "The girl has shouted.",
            "The girl did shout.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject\n"
            "• clamavit (shouted) — verb, perfect tense (the -v- marker), he/she form"
        ),
    },
    {
        "latin": "pater feminam rogavit.",
        "english": [
            "The father asked the woman.",
            "The father has asked the woman.",
            "The father questioned the woman.",
            "The father did ask the woman.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject\n"
            "• feminam (woman) — accusative singular, direct object\n"
            "• rogavit (asked) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "dea pulchra deum amavit, et deus clamavit.",
        "english": [
            "The beautiful goddess loved the god, and the god shouted.",
            "The beautiful goddess has loved the god, and the god has shouted.",
            "The beautiful goddess liked the god, and the god cried out.",
            "The beautiful goddess loved the god, and the god called out.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject of first clause\n"
            "• pulchra (beautiful) — adjective agreeing with dea\n"
            "• deum (god) — accusative singular, direct object\n"
            "• amavit (loved) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• deus (god) — nominative singular, subject of second clause\n"
            "• clamavit (shouted) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "regina filiam non liberaverat, sed pater domum festinavit.",
        "english": [
            "The queen had not freed the daughter, but the father hurried home.",
            "The queen had not set free the daughter, but the father hurried home.",
            "The queen had not freed her daughter, but the father hurried homewards.",
            "The queen had not freed the daughter, but the father has hurried home.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject of first clause\n"
            "• filiam (daughter) — accusative singular, direct object\n"
            "• non (not) — negates the verb\n"
            "• liberaverat (had freed) — verb, pluperfect tense (-verat ending), he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• domum (home) — accusative of motion (no preposition needed)\n"
            "• festinavit (hurried) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "multi dei ad insulam navigaverunt, et puellas necaverunt.",
        "english": [
            "Many gods sailed to the island, and killed the girls.",
            "Many gods sailed towards the island, and killed the girls.",
            "Many gods have sailed to the island, and have killed the girls.",
            "Many of the gods sailed to the island, and murdered the girls.",
        ],
        "explanation": (
            "• multi (many) — adjective agreeing with dei\n"
            "• dei (gods) — nominative plural, subject\n"
            "• ad insulam (to the island) — prepositional phrase: ad + accusative\n"
            "• navigaverunt (sailed) — verb, perfect tense, they form\n"
            "• et (and) — coordinating conjunction\n"
            "• puellas (girls) — accusative plural, direct object\n"
            "• necaverunt (killed) — verb, perfect tense, they form"
        ),
    },
    {
        "latin": "pater ingens puellam amaverat, sed puella tristis deum oraverat.",
        "english": [
            "The huge father had loved the girl, but the sad girl had begged the god.",
            "The enormous father had loved the girl, but the unhappy girl had begged the god.",
            "The huge father had liked the girl, but the sad girl had pleaded with the god.",
            "The huge father had loved the girl, but the sad girl had prayed to the god.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject of first clause\n"
            "• ingens (huge) — adjective agreeing with pater\n"
            "• puellam (girl) — accusative singular, direct object\n"
            "• amaverat (had loved) — verb, pluperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• puella (girl) — nominative singular, subject of second clause\n"
            "• tristis (sad) — adjective agreeing with puella\n"
            "• deum (god) — accusative singular, direct object\n"
            "• oraverat (had begged) — verb, pluperfect tense, he/she form"
        ),
    },
    {
        # REWRITTEN: original "illa dea ad feminam appropinquavit, nam tam tristis erat."
        # removed 'tam' (Node 5) and 'erat' (Node 5). New sentence still uses illa + appropinquavit.
        "latin": "illa dea ad tristem feminam appropinquavit, et clamabat.",
        "english": [
            "That goddess approached the sad woman, and was shouting.",
            "That goddess drew near to the sad woman, and was shouting.",
            "That goddess came near to the unhappy woman, and kept shouting.",
            "The goddess approached the sad woman, and was shouting.",
        ],
        "explanation": (
            "• illa (that) — demonstrative agreeing with dea\n"
            "• dea (goddess) — nominative singular, subject\n"
            "• ad tristem feminam (to the sad woman) — prepositional phrase: ad + accusative\n"
            "• appropinquavit (approached) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• clamabat (was shouting) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "regina urbem oppugnavit, et prope insulam habitavit.",
        "english": [
            "The queen attacked the city, and lived near the island.",
            "The queen has attacked the city, and has lived near the island.",
            "The queen attacked the city, and dwelt close to the island.",
            "The queen attacked the city, and lived next to the island.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject\n"
            "• urbem (city) — accusative singular, direct object\n"
            "• oppugnavit (attacked) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• prope insulam (near the island) — prepositional phrase: prope + accusative\n"
            "• habitavit (lived) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "ego deos rogaveram, sed etiam tum non clamaverant.",
        "english": [
            "I had asked the gods, but even then they had not shouted.",
            "I myself had asked the gods, but still then they had not shouted.",
            "I had asked the gods, but also then they had not shouted.",
            "I had asked the gods, but even at that moment they had not shouted.",
        ],
        "explanation": (
            "• ego (I) — nominative singular, emphatic subject\n"
            "• deos (gods) — accusative plural, direct object\n"
            "• rogaveram (had asked) — verb, pluperfect tense, I form\n"
            "• sed (but) — coordinating conjunction\n"
            "• etiam (even / also / still) — adverb\n"
            "• tum (then) — adverb\n"
            "• non (not) — negates the verb\n"
            "• clamaverant (had shouted) — verb, pluperfect tense, they form (subject = the gods)"
        ),
    },
    {
        "latin": "pater mihi imperavit, et dea feminam pulchram putaverat.",
        "english": [
            "The father ordered me, and the goddess had thought the woman beautiful.",
            "The father ordered me, and the goddess had considered the woman beautiful.",
            "The father has ordered me, and the goddess had thought the woman (to be) beautiful.",
            "The father ordered me, and the goddess had thought (that) the woman (was) beautiful.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject of first clause\n"
            "• mihi (me) — DATIVE singular pronoun (impero takes the dative — not 'to me')\n"
            "• imperavit (ordered) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• feminam (woman) — accusative singular, direct object\n"
            "• pulchram (beautiful) — adjective agreeing with feminam — 'double accusative' with puto: 'think X (to be) Y'\n"
            "• putaverat (had thought) — verb, pluperfect tense, he/she form"
        ),
    },
]

# Set 14 — PPP / Passive review
# Strict ideal = "having been X-ed"
SENTENCES_N1_SET14 = [
    {
        "latin": "puella liberata clamavit.",
        "english": [
            "The girl, having been freed, shouted.",
            "The freed girl shouted.",
            "The girl who had been freed shouted.",
            "Once freed, the girl shouted.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject\n"
            "• liberata (having been freed) — PPP, nominative singular feminine, agreeing with puella\n"
            "• clamavit (shouted) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "femina necata erat.",
        "english": [
            "The woman had been killed.",
            "The woman had been murdered.",
        ],
        "explanation": (
            "• femina (woman) — nominative singular, subject\n"
            "• necata (killed) — PPP, nominative singular feminine, agreeing with femina\n"
            "• erat (had been) — auxiliary forming the pluperfect passive with necata"
        ),
    },
    {
        "latin": "dea oppugnata ad insulam navigabat.",
        "english": [
            "The goddess, having been attacked, was sailing to the island.",
            "The goddess, having been attacked, was sailing towards the island.",
            "The attacked goddess was sailing to the island.",
            "The goddess who had been attacked was sailing towards the island.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject\n"
            "• oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with dea\n"
            "• ad insulam (to the island) — prepositional phrase: ad + accusative\n"
            "• navigabat (was sailing) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "pater filiam amatam rogavit.",
        "english": [
            "The father asked the having-been-loved daughter.",
            "The father asked the daughter who had been loved.",
            "The father asked his beloved daughter.",
            "The father questioned the loved daughter.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject\n"
            "• filiam (daughter) — accusative singular, direct object\n"
            "• amatam (having been loved) — PPP, accusative singular feminine, agreeing with filiam\n"
            "• rogavit (asked) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "regina liberata puellam tristem amavit.",
        "english": [
            "The queen, having been freed, loved the sad girl.",
            "The freed queen loved the sad girl.",
            "The queen, once freed, loved the unhappy girl.",
            "The queen who had been freed liked the sad girl.",
        ],
        "explanation": (
            "• regina (queen) — nominative singular, subject\n"
            "• liberata (having been freed) — PPP, nominative singular feminine, agreeing with regina\n"
            "• puellam (girl) — accusative singular, direct object\n"
            "• tristem (sad) — adjective, accusative singular, agreeing with puellam\n"
            "• amavit (loved) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "deus necatus erat, et dea clamabat.",
        "english": [
            "The god had been killed, and the goddess was shouting.",
            "The god had been murdered, and the goddess kept shouting.",
            "The god had been killed, and the goddess used to shout.",
            "The god had been killed, and the goddess was shouting.",
        ],
        "explanation": (
            "• deus (god) — nominative singular, subject of first clause\n"
            "• necatus (killed) — PPP, nominative singular masculine, agreeing with deus\n"
            "• erat (had been) — auxiliary forming the pluperfect passive with necatus\n"
            "• et (and) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• clamabat (was shouting) — verb, imperfect tense, he/she form"
        ),
    },
    {
        "latin": "multae feminae oratae erant, sed reginae laetae non festinaverunt.",
        "english": [
            "Many women had been begged, but the happy queens did not hurry.",
            "Many women had been pleaded with, but the joyful queens did not hurry.",
            "Many women had been prayed to, but the happy queens did not rush.",
            "Many women had been begged, but the happy queens did not hurry.",
        ],
        "explanation": (
            "• multae (many) — adjective agreeing with feminae\n"
            "• feminae (women) — nominative plural, subject of first clause\n"
            "• oratae (begged) — PPP, nominative plural feminine, agreeing with feminae\n"
            "• erant (had been) — auxiliary forming the pluperfect passive with oratae\n"
            "• sed (but) — coordinating conjunction\n"
            "• reginae (queens) — nominative plural, subject of second clause\n"
            "• laetae (happy) — adjective agreeing with reginae\n"
            "• non (not) — negates the verb\n"
            "• festinaverunt (hurried) — verb, perfect tense, they form"
        ),
    },
    {
        "latin": "puella oppugnata patrem oravit, et pater feminas liberavit.",
        "english": [
            "The girl, having been attacked, begged the father, and the father freed the women.",
            "The attacked girl begged her father, and the father set free the women.",
            "The girl who had been attacked pleaded with the father, and the father freed the women.",
            "Once attacked, the girl begged the father, and the father freed the women.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with puella\n"
            "• patrem (father) — accusative singular, direct object\n"
            "• oravit (begged) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• feminas (women) — accusative plural, direct object\n"
            "• liberavit (freed) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "dea tristis deum necatum amaverat, sed deus imperatus erat.",
        "english": [
            "The sad goddess had loved the having-been-killed god, but the god had been ordered.",
            "The sad goddess had loved the killed god, but the god had been commanded.",
            "The unhappy goddess had loved the god who had been killed, but the god had been given orders.",
            "The sad goddess had loved the slain god, but the god had been ordered.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject of first clause\n"
            "• tristis (sad) — adjective agreeing with dea\n"
            "• deum (god) — accusative singular, direct object\n"
            "• necatum (having been killed) — PPP, accusative singular masculine, agreeing with deum\n"
            "• amaverat (had loved) — verb, pluperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• deus (god) — nominative singular, subject of second clause\n"
            "• imperatus (ordered) — PPP, nominative singular masculine, agreeing with deus\n"
            "• erat (had been) — auxiliary forming the pluperfect passive with imperatus"
        ),
    },
    {
        "latin": "ingens navis oppugnata ad terram navigabat, et multi dei clamaverunt.",
        "english": [
            "The huge ship, having been attacked, was sailing to the land, and many gods shouted.",
            "The enormous ship, having been attacked, was sailing towards the land, and many gods shouted.",
            "The huge attacked ship was sailing to the land, and many gods shouted.",
            "The vast ship, once attacked, was sailing to the land, and many gods shouted.",
        ],
        "explanation": (
            "• ingens (huge) — adjective agreeing with navis\n"
            "• navis (ship) — nominative singular, subject of first clause\n"
            "• oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with navis\n"
            "• ad terram (to the land) — prepositional phrase: ad + accusative\n"
            "• navigabat (was sailing) — verb, imperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• multi (many) — adjective agreeing with dei\n"
            "• dei (gods) — nominative plural, subject of second clause\n"
            "• clamaverunt (shouted) — verb, perfect tense, they form"
        ),
    },
]

# Set 16 — Exam-level mixed
SENTENCES_N1_SET16 = [
    {
        "latin": "illa puella pulchra reginam oraverat, et dea puellam liberavit.",
        "english": [
            "That beautiful girl had begged the queen, and the goddess freed the girl.",
            "That beautiful girl had pleaded with the queen, and the goddess set free the girl.",
            "That famous beautiful girl had prayed to the queen, and the goddess freed the girl.",
            "That beautiful girl had begged the queen, and the goddess has freed the girl.",
        ],
        "explanation": (
            "• illa (that) — demonstrative agreeing with puella\n"
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• pulchra (beautiful) — adjective agreeing with puella\n"
            "• reginam (queen) — accusative singular, direct object\n"
            "• oraverat (had begged) — verb, pluperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• puellam (girl) — accusative singular, direct object\n"
            "• liberavit (freed) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "multi dei ad ingentem urbem navigaverunt feminasque necaverunt.",
        "english": [
            "Many gods sailed to the huge city and killed the women.",
            "Many gods sailed towards the enormous city, and killed the women.",
            "Many of the gods sailed to the huge city and murdered the women.",
            "Many gods sailed to the huge city, and they killed the women.",
        ],
        "explanation": (
            "• multi (many) — adjective agreeing with dei\n"
            "• dei (gods) — nominative plural, subject\n"
            "• ad ingentem urbem (to the huge city) — prepositional phrase: ad + accusative\n"
            "• navigaverunt (sailed) — verb, perfect tense, they form\n"
            "• feminas (women) — accusative plural, direct object\n"
            "• -que (and) — attached to feminas, joining the two verbs\n"
            "• necaverunt (killed) — verb, perfect tense, they form"
        ),
    },
    {
        "latin": "pater tristis filiam amatam liberaverat, sed dea puellam oppugnavit.",
        "english": [
            "The sad father had freed the having-been-loved daughter, but the goddess attacked the girl.",
            "The unhappy father had freed the loved daughter, but the goddess attacked the girl.",
            "The sad father had set free his beloved daughter, but the goddess attacked the girl.",
            "The sad father had freed the daughter who had been loved, but the goddess attacked the girl.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject of first clause\n"
            "• tristis (sad) — adjective agreeing with pater\n"
            "• filiam (daughter) — accusative singular, direct object\n"
            "• amatam (having been loved) — PPP, accusative singular feminine, agreeing with filiam\n"
            "• liberaverat (had freed) — verb, pluperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• dea (goddess) — nominative singular, subject of second clause\n"
            "• puellam (girl) — accusative singular, direct object\n"
            "• oppugnavit (attacked) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "illa regina tum in insula habitabat, nam dei patrem necaverant.",
        "english": [
            "That queen was then living on the island, for the gods had killed the father.",
            "That queen used to live on the island then, for the gods had killed the father.",
            "That famous queen was living on the island then, because the gods had killed the father.",
            "That queen was living on the island then, for the gods had killed her father.",
        ],
        "explanation": (
            "• illa (that) — demonstrative agreeing with regina\n"
            "• regina (queen) — nominative singular, subject of first clause\n"
            "• tum (then) — adverb (flexible position)\n"
            "• in insula (on the island) — prepositional phrase: in + ablative\n"
            "• habitabat (was living) — verb, imperfect tense, he/she form\n"
            "• nam (for) — conjunction introducing a reason\n"
            "• dei (gods) — nominative plural, subject of second clause\n"
            "• patrem (father) — accusative singular, direct object\n"
            "• necaverant (had killed) — verb, pluperfect tense, they form"
        ),
    },
    {
        "latin": "femina pulchra deum rogavit, sed deus illud non putavit.",
        "english": [
            "The beautiful woman asked the god, but the god did not think that.",
            "The beautiful woman questioned the god, but the god did not think that.",
            "The beautiful woman asked the god, but the god did not believe that.",
            "The beautiful woman asked the god, but the god did not think so.",
        ],
        "explanation": (
            "• femina (woman) — nominative singular, subject of first clause\n"
            "• pulchra (beautiful) — adjective agreeing with femina\n"
            "• deum (god) — accusative singular, direct object\n"
            "• rogavit (asked) — verb, perfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• deus (god) — nominative singular, subject of second clause\n"
            "• illud (that thing) — neuter demonstrative, accusative, direct object\n"
            "• non (not) — negates the verb\n"
            "• putavit (thought) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "dea ad terram ingentem navigabat, et puellae oppugnatae clamabant.",
        "english": [
            "The goddess was sailing to the huge land, and the having-been-attacked girls were shouting.",
            "The goddess was sailing towards the enormous land, and the attacked girls were shouting.",
            "The goddess used to sail to the vast land, and the girls who had been attacked were shouting.",
            "The goddess was sailing to the huge country, and the attacked girls kept shouting.",
        ],
        "explanation": (
            "• dea (goddess) — nominative singular, subject of first clause\n"
            "• ad terram ingentem (to the huge land) — prepositional phrase: ad + accusative; ingentem agrees with terram\n"
            "• navigabat (was sailing) — verb, imperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• puellae (girls) — nominative plural, subject of second clause\n"
            "• oppugnatae (having been attacked) — PPP, nominative plural feminine, agreeing with puellae\n"
            "• clamabant (were shouting) — verb, imperfect tense, they form"
        ),
    },
    {
        "latin": "pater ad insulam appropinquavit, et filiam oppugnatam liberavit.",
        "english": [
            "The father approached to the island, and freed the having-been-attacked daughter.",
            "The father drew near to the island, and freed the attacked daughter.",
            "The father came near to the island, and set free the daughter who had been attacked.",
            "The father approached the island, and freed his attacked daughter.",
        ],
        "explanation": (
            "• pater (father) — nominative singular, subject\n"
            "• ad insulam (to the island) — prepositional phrase: ad + accusative\n"
            "• appropinquavit (approached) — verb, perfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• filiam (daughter) — accusative singular, direct object\n"
            "• oppugnatam (having been attacked) — PPP, accusative singular feminine, agreeing with filiam\n"
            "• liberavit (freed) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "multi dei reginam tristem oraverant, sed regina deis non imperavit.",
        "english": [
            "Many gods had begged the sad queen, but the queen did not order the gods.",
            "Many gods had pleaded with the unhappy queen, but the queen did not order the gods.",
            "Many of the gods had prayed to the sad queen, but the queen did not command the gods.",
            "Many gods had begged the sad queen, but the queen has not ordered the gods.",
        ],
        "explanation": (
            "• multi (many) — adjective agreeing with dei\n"
            "• dei (gods) — nominative plural, subject of first clause\n"
            "• reginam (queen) — accusative singular, direct object\n"
            "• tristem (sad) — adjective agreeing with reginam\n"
            "• oraverant (had begged) — verb, pluperfect tense, they form\n"
            "• sed (but) — coordinating conjunction\n"
            "• regina (queen) — nominative singular, subject of second clause\n"
            "• deis (gods) — DATIVE plural (impero takes the dative — not 'to the gods')\n"
            "• non (not) — negates the verb\n"
            "• imperavit (ordered) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "puella liberata in urbem festinabat, et pater deam tum oravit.",
        "english": [
            "The girl, having been freed, was hurrying into the city, and the father then begged the goddess.",
            "The freed girl was hurrying into the city, and then the father begged the goddess.",
            "The girl who had been freed was rushing to the city, and the father pleaded with the goddess then.",
            "Once freed, the girl was hurrying into the city, and the father prayed to the goddess then.",
        ],
        "explanation": (
            "• puella (girl) — nominative singular, subject of first clause\n"
            "• liberata (having been freed) — PPP, nominative singular feminine, agreeing with puella\n"
            "• in urbem (into the city) — prepositional phrase: in + accusative = into\n"
            "• festinabat (was hurrying) — verb, imperfect tense, he/she form\n"
            "• et (and) — coordinating conjunction\n"
            "• pater (father) — nominative singular, subject of second clause\n"
            "• deam (goddess) — accusative singular, direct object\n"
            "• tum (then) — adverb (flexible position)\n"
            "• oravit (begged) — verb, perfect tense, he/she form"
        ),
    },
    {
        "latin": "ille deus pulchras feminas oppugnatas amaverat, sed reginae tristes clamaverant.",
        "english": [
            "That god had loved the beautiful having-been-attacked women, but the sad queens had shouted.",
            "That god had loved the beautiful attacked women, but the unhappy queens had shouted.",
            "That famous god had liked the beautiful women who had been attacked, but the sad queens had shouted.",
            "That god had loved the beautiful attacked women, but the sad queens had cried out.",
        ],
        "explanation": (
            "• ille (that) — demonstrative agreeing with deus\n"
            "• deus (god) — nominative singular, subject of first clause\n"
            "• pulchras (beautiful) — adjective agreeing with feminas\n"
            "• feminas (women) — accusative plural, direct object\n"
            "• oppugnatas (having been attacked) — PPP, accusative plural feminine, agreeing with feminas\n"
            "• amaverat (had loved) — verb, pluperfect tense, he/she form\n"
            "• sed (but) — coordinating conjunction\n"
            "• reginae (queens) — nominative plural, subject of second clause\n"
            "• tristes (sad) — adjective agreeing with reginae\n"
            "• clamaverant (had shouted) — verb, pluperfect tense, they form"
        ),
    },
]

# ════════════════════════════════════════════════════════════════════════════
# Parse-translate: Node 1 — only 1st-conjugation verbs across all tenses
# ════════════════════════════════════════════════════════════════════════════

PARSE_TRANSLATE_NODE1 = [
    # Present
    {"form":"rogat",         "tense":"present",    "person":"3rd","number":"singular", "translation":"he/she asks"},
    {"form":"clamant",       "tense":"present",    "person":"3rd","number":"plural",   "translation":"they shout"},
    {"form":"habito",        "tense":"present",    "person":"1st","number":"singular", "translation":"I live"},
    {"form":"amatis",        "tense":"present",    "person":"2nd","number":"plural",   "translation":"you (pl) love"},
    # Imperfect
    {"form":"necabat",       "tense":"imperfect",  "person":"3rd","number":"singular", "translation":"he/she was killing"},
    {"form":"navigabamus",   "tense":"imperfect",  "person":"1st","number":"plural",   "translation":"we were sailing"},
    {"form":"imperabant",    "tense":"imperfect",  "person":"3rd","number":"plural",   "translation":"they were ordering"},
    # Future
    {"form":"amabit",        "tense":"future",     "person":"3rd","number":"singular", "translation":"he/she will love"},
    {"form":"oppugnabunt",   "tense":"future",     "person":"3rd","number":"plural",   "translation":"they will attack"},
    {"form":"festinabis",    "tense":"future",     "person":"2nd","number":"singular", "translation":"you (sg) will hurry"},
    # Perfect
    {"form":"clamavit",      "tense":"perfect",    "person":"3rd","number":"singular", "translation":"he/she shouted"},
    {"form":"liberaverunt",  "tense":"perfect",    "person":"3rd","number":"plural",   "translation":"they freed"},
    {"form":"oravi",         "tense":"perfect",    "person":"1st","number":"singular", "translation":"I begged"},
    # Pluperfect
    {"form":"putaverat",     "tense":"pluperfect", "person":"3rd","number":"singular", "translation":"he/she had thought"},
    {"form":"rogaverant",    "tense":"pluperfect", "person":"3rd","number":"plural",   "translation":"they had asked"},
]
