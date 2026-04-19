import json

VERBS = [
    ("ama", "amav", "love", "loved", "loving"),
    ("clama", "clamav", "shout", "shouted", "shouting"),
    ("roga", "rogav", "ask", "asked", "asking"),
    ("ambula", "ambulav", "walk", "walked", "walking"),
    ("festina", "festinav", "hurry", "hurried", "hurrying")
]

TENSES = {
    "present": [
        ("o", "I {0}"), ("s", "you (sg) {0}"), ("t", "he/she {0}s"), 
        ("mus", "we {0}"), ("tis", "you (pl) {0}"), ("nt", "they {0}")
    ],
    "imperfect": [
        ("bam", "I was {ing}"), ("bas", "you (sg) were {ing}"), ("bat", "he/she was {ing}"), 
        ("bamus", "we were {ing}"), ("batis", "you (pl) were {ing}"), ("bant", "they were {ing}")
    ],
    "future": [
        ("bo", "I will {0}"), ("bis", "you (sg) will {0}"), ("bit", "he/she will {0}"), 
        ("bimus", "we will {0}"), ("bitis", "you (pl) will {0}"), ("bunt", "they will {0}")
    ],
    "perfect": [
        ("i", "I {ed}"), ("isti", "you (sg) {ed}"), ("it", "he/she {ed}"), 
        ("imus", "we {ed}"), ("istis", "you (pl) {ed}"), ("erunt", "they {ed}")
    ],
    "pluperfect": [
        ("eram", "I had {ed}"), ("eras", "you (sg) had {ed}"), ("erat", "he/she had {ed}"), 
        ("eramus", "we had {ed}"), ("eratis", "you (pl) had {ed}"), ("erant", "they had {ed}")
    ]
}

def generate_questions(tense):
    questions = []
    
    stem_idx = 0 if tense in ("present", "imperfect", "future") else 1
    
    for v in VERBS:
        pr_stem, pf_stem, base_eng, past_eng, ing_eng = v
        stem = pr_stem if stem_idx == 0 else pf_stem
        
        for suffix, eng_template in TENSES[tense]:
            form = stem + suffix
            if tense == "future" and suffix == "bo": form = stem[:-1] + "abo"
            if tense == "present" and suffix == "o": form = stem[:-1] + "o" # ama + o -> amo
            
            # Form answer
            if "{ing}" in eng_template: ans = eng_template.format(ing=ing_eng)
            elif "{ed}" in eng_template: ans = eng_template.format(ed=past_eng)
            elif "{0}s" in eng_template: # he/she fixes
                if base_eng == "hurry": ans = eng_template.format("hurrie") # he/she hurries
                else: ans = eng_template.format(base_eng)
            elif "{0}" in eng_template: ans = eng_template.format(base_eng)
                
            options = [ans]
            for osuffix, oeng_template in TENSES[tense]:
                if osuffix != suffix:
                    if "{ing}" in oeng_template: o_ans = oeng_template.format(ing=ing_eng)
                    elif "{ed}" in oeng_template: o_ans = oeng_template.format(ed=past_eng)
                    elif "{0}s" in oeng_template:
                        if base_eng == "hurry": o_ans = oeng_template.format("hurrie")
                        else: o_ans = oeng_template.format(base_eng)
                    elif "{0}" in oeng_template: o_ans = oeng_template.format(base_eng)
                    options.append(o_ans)
            
            import random
            random.seed(hash(form))
            Wrongs = options[1:]
            random.shuffle(Wrongs)
            final_opts = [ans] + Wrongs[:3]
            random.shuffle(final_opts)
            
            questions.append({"form": form, "correct": ans, "options": final_opts})
            
    return questions

with open("generated_sets.txt", "w") as f:
    for t in ("present", "imperfect", "future", "perfect", "pluperfect"):
        f.write(f"QUESTIONS_{t.upper()} = [\n")
        for q in generate_questions(t):
            f.write(f"    {json.dumps(q)},\n")
        f.write("]\n\n")

print("Generated questions!")
