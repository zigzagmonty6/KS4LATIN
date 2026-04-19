"""Canonical glosses — sourced VERBATIM from the teacher's official word list.

RULES:
  - Do not paraphrase. Do not reorder senses. Do not "improve" wording.
  - If a card shows a Latin lemma to a pupil, its English gloss MUST come from here.
  - If a gloss is missing, add it — do not invent one on the fly.

The keys are the display-form of the lemma as it appears on the card.
The values are the teacher-authoritative English gloss (exact string).
"""

OFFICIAL_GLOSSES = {
    # ── Node 1 lemmas ────────────────────────────────────────────────────
    # Nouns
    "puella":  "girl",
    "dea":     "goddess",
    "femina":  "woman",
    "pater":   "father",
    "filia":   "daughter",
    "insula":  "island, block of flats",
    "regina":  "queen",
    "deus":    "god",
    "terra":   "land, earth, ground",
    "urbs":    "city",
    "navis":   "ship",
    "domum":   "(to) home",
    # Adjectives
    "pulcher": "beautiful",
    "tristis": "sad",
    "laetus":  "happy",
    "ingens":  "huge",
    "multus":  "much, many",
    # Pronouns
    "ego":     "I",
    "me":      "me",
    "mihi":    "to/for me",
    # Demonstratives (one card covers all three genders per teacher list)
    "ille, illa, illud": "he, she, it; that (those)",
    "hic, haec, hoc":    "this (these)",
    # Prepositions
    "in + acc": "into, onto",
    "in + abl": "in, on",
    "ad":       "to, towards, at",
    "per":      "through",
    "prope":    "near",
    "e, ex":    "from, out of",
    "a, ab":    "(away) from",
    "cum + abl":"with",
    "cum + subj":"when, since",
    "ut + subj":"(so) that, (in order) to",
    # Conjunctions / adverbs
    "et":       "and",
    "sed":      "but",
    "nam":      "for",
    "-que":     "and",
    "non":      "not",
    "ibi":      "there",
    "tum":      "then",
    "subito":   "suddenly",
    "etiam":    "even, also",
    "tamen":    "however",
    "iam":      "now, already",
    "nunc":     "now",
    "mox":      "soon",
    "vix":      "hardly, scarcely",
    "statim":   "at once, immediately",
    "tandem":   "finally, at last",
    "deinde":   "then",
    "enim":     "for",
    "igitur":   "therefore",
    "iterum":   "again",
    "quamquam": "although",
    "postquam": "after",
    "dum":      "while",
    "si":       "if",
    "ubi":      "when, where",
    "simulac":  "as soon as",
    "cur":      "why",
    "quo modo": "how",
    "tam":      "so",

    # ── Verbs (1st-person singular present = teacher card face) ─────────
    "amo":         "I love",
    "rogo":        "I ask",
    "habito":      "I live",
    "navigo":      "I sail",
    "clamo":       "I shout",
    "appropinquo": "I approach",
    "impero":      "I order",
    "festino":     "I hurry",
    "oro":         "I beg",
    "oppugno":     "I attack",
    "libero":      "I free",
    "neco":        "I kill",
    "puto":        "I think",
    # Other verbs present in later nodes (sourced from list — used by
    # Nodes 2–6 when we rewrite them):
    "video; vidi":   "I see; I saw",
    "esse(t)":       "to be, he/she/it was",
    "est":           "(he/she/it/there) is",
    "erat":          "(he/she/it/there) was",
    "conspexi":      "I noticed",
    "facio; feci":   "I make, do; I made, did",
    "habeo":         "I have",
    "inquit":        "he/she says, said",
    "duco":          "I lead",
    "occido":        "I kill",
    "advenio":       "I arrive",
    "iussi":         "I ordered",
    "persuadeo":     "I persuade",
    "cognosco":      "I get to know, find out",
    "cognovi":       "I got to know, found out",
    "dico; dixi":    "I say; I said",
    "volo":          "I want",
    "dormio":        "I sleep",
    "audio":         "I hear, listen",
    "pono":          "I put, place",
    "posui":         "I put, placed",
    "posse(t)":      "to be able, he/she/it was able",
    "aperio":        "I open",
    "apertus":       "(having been) opened",
    "cupio":         "I want",
    "peto":          "I seek, beg, ask, attack",
    "quaero":        "I search, ask (for)",
    "cogo":          "I force",
    "coactus":       "(having been) forced",
    "appareo":       "I appear",
    "redire(t)":     "to return, (s)he was returning",
    "rediit":        "he/she returned",
    "accepi":        "I accepted, received",
    "consilium cepi":"I had an idea",
    "constituo":     "I decide",
    "relinquo":      "I leave behind",
    "coepi":         "I begin",
    "effugio":       "I escape",
    "eo":            "I leave",
    "discessi":      "I left",
    "teneo":         "I hold",
    "noli(te)":      "don't",
    "conatur":       "he/she tries",

    # Later-node nouns / adjectives / pronouns / etc.
    "homo":       "man, human",
    "iuvenis":    "young (man)",
    "rex":        "king",
    "vir":        "man",
    "miles":      "soldier",
    "dux":        "leader",
    "silva":      "wood",
    "filius":     "son",
    "uxor":       "wife",
    "maritus":    "husband",
    "comes":      "companion",
    "amicus":     "friend",
    "equus":      "horse",
    "caput":      "head",
    "manus":      "hand, group",
    "vultus":     "face, expression",
    "mors":       "death",
    "iter":       "journey",
    "gladius":    "sword",
    "porta":      "gate",
    "cibus":      "food",
    "donum":      "gift",
    "verbum":     "word",
    "annus":      "year",
    "iratus":     "angry",
    "fortis":     "brave, strong",
    "solus":      "alone, lonely",
    "dirus":      "dreadful",
    "facilis":    "easy",
    "omnis":      "all, every",
    "unus":       "one",
    "pauci":      "a few",
    "alius":      "other, another",
    "tantus":     "so great, such a great",
    "suus":       "his, her, its, their",
    "ceteri":     "the rest",
    "necesse":    "necessary",
    "nihil":      "nothing",
    "tu, te":     "you (sg)",
    "se":         "him-, her-, it(self); them(selves)",
    "eum; eam":   "him, it; her, it",
    "eos, eas":   "them",
    "ei":         "to/for him, her, it",
    "eius":       "his, her, its; of him, her, it",
    "qui, quae":  "who, which",
    "quod":       "because, which",
    "quam":       "than, whom, which, how",
}


def g(lemma: str) -> str:
    """Look up the official gloss; fail loudly if missing.

    If you get a KeyError, STOP: add the entry to the teacher's list, not
    here. Silent fallbacks are how definitions drifted before.
    """
    try:
        return OFFICIAL_GLOSSES[lemma]
    except KeyError as e:
        raise KeyError(
            f"No official gloss for {lemma!r}. Add it to OFFICIAL_GLOSSES "
            f"(sourced from the teacher's word list) before using."
        ) from e
