"""Derive per-node vocab from parsed sentences.

Strategy: build a form→lemma map from GLOSS_MASTER.json keys + generated inflections,
tokenise each sentence, and for each lemma record the earliest (node, set) where it appears.
"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

P = r'C:/Users/mmhun/Desktop/y11_latin_gcse/'
sents = json.load(open(P + '_sentences_parsed.json', 'r', encoding='utf-8'))
gloss = json.load(open(P + 'y11/GLOSS_MASTER.json', 'r', encoding='utf-8'))['glosses']

# --- Build form→lemma map from gloss keys + hand-crafted forms ---
# Lemmas stored as canonical lemma strings; forms map to them.
form2lemma = {}

def add(lemma, forms):
    for f in forms:
        form2lemma[f.lower()] = lemma

# 1st-conj verbs (present/imperfect/future/perfect/pluperfect/PPP forms)
V1 = ['amo','clamo','festino','habito','impero','libero','navigo','neco','oppugno','oro','puto','rogo','appropinquo']
for v in V1:
    stem = v[:-1]  # amo → am
    # present: -o, -as, -at, -amus, -atis, -ant
    add(v, [v, stem+'as', stem+'at', stem+'amus', stem+'atis', stem+'ant'])
    # imperfect: -abam/-abas/-abat/-abamus/-abatis/-abant
    add(v, [stem+'abam', stem+'abas', stem+'abat', stem+'abamus', stem+'abatis', stem+'abant'])
    # future: -abo/-abis/-abit/-abimus/-abitis/-abunt
    add(v, [stem+'abo', stem+'abis', stem+'abit', stem+'abimus', stem+'abitis', stem+'abunt'])
    # perfect: -avi/-avisti/-avit/-avimus/-avistis/-averunt (-arunt)
    add(v, [stem+'avi', stem+'avisti', stem+'avit', stem+'avimus', stem+'avistis', stem+'averunt', stem+'arunt'])
    # pluperfect: -averam/-averas/-averat/-averamus/-averatis/-averant
    add(v, [stem+'averam', stem+'averas', stem+'averat', stem+'averant'])
    # PPP + forms: -atus/-ata/-atum + declensions (simplified)
    for ending in ['atus','ata','atum','ati','atae','atos','atas','ato','atis','atam','ate']:
        add(v, [stem+ending])
    # infinitive + imperative + participle
    add(v, [stem+'are', stem+'a', stem+'ate', stem+'ans', stem+'antis'])

# 2nd-conj: habeo, teneo, video, iubeo, persuadeo, appareo, moneo (moneo not glossed but prescribed)
V2 = {
    'habeo': 'hab', 'teneo': 'ten', 'video': 'vid', 'iubeo': 'iub', 'persuadeo': 'persuad',
    'appareo': 'appar', 'moneo': 'mon'
}
for v, stem in V2.items():
    add(v, [v, stem+'es', stem+'et', stem+'emus', stem+'etis', stem+'ent'])
    add(v, [stem+'ebam', stem+'ebas', stem+'ebat', stem+'ebamus', stem+'ebatis', stem+'ebant'])
    add(v, [stem+'ebo', stem+'ebis', stem+'ebit', stem+'ebimus', stem+'ebitis', stem+'ebunt'])
    add(v, [stem+'ere'])
    # perfect stems per verb
    perf = {'habeo':'habu','teneo':'tenu','video':'vid','iubeo':'iuss','persuadeo':'persuas','appareo':'apparu','moneo':'monu'}[v]
    for pe in ['i','isti','it','imus','istis','erunt']:
        add(v, [perf+pe])
    for pe in ['eram','eras','erat','eramus','eratis','erant']:
        add(v, [perf+pe])
    # PPP per verb
    ppp = {'habeo':'habit','teneo':'tent','video':'vis','iubeo':'iuss','persuadeo':'persuas','appareo':'apparit','moneo':'monit'}[v]
    for end in ['us','a','um','i','ae','os','as','o','is','am','e']:
        add(v, [ppp+end])

# 3rd-conj: capio, cogo, cognosco, conspicio, constituo, cupio, dico, discedo, duco, effugio, facio, occido, peto, pono, quaero, relinquo
V3 = {
    'capio':('capi','cep','capt'), 'cogo':('cog','coeg','coact'), 'cognosco':('cognosc','cognov','cognit'),
    'conspicio':('conspici','conspex','conspect'), 'constituo':('constitu','constitu','constitut'),
    'cupio':('cupi','cupiv','cupit'), 'dico':('dic','dix','dict'), 'discedo':('disced','discess','discess'),
    'duco':('duc','dux','duct'), 'effugio':('effugi','effug','effugit'), 'facio':('faci','fec','fact'),
    'occido':('occid','occid','occis'), 'peto':('pet','petiv','petit'), 'pono':('pon','posu','posit'),
    'quaero':('quaer','quaesiv','quaesit'), 'relinquo':('relinqu','reliqu','relict'),
    'accipio':('accipi','accep','accept'),
}
for v,(pres,perf,ppp) in V3.items():
    # present: like duco → dux... stems tricky. Use -o/-is/-it/-imus/-itis/-unt (or -iunt for -io)
    io = pres.endswith('i')
    base = pres[:-1] if io else pres
    add(v, [v, base+'is' if not io else pres+'s', base+'it' if not io else pres+'t',
            base+'imus' if not io else pres+'mus', base+'itis' if not io else pres+'tis',
            base+'unt' if not io else pres+'unt'])
    # also plain -is/-it for -io as capis? No: capio→capis/capit/capimus/capitis/capiunt
    if io:
        add(v, [pres+'s', pres+'t', pres+'mus', pres+'tis', pres+'unt'])
    # imperfect -ebam etc
    for e in ['ebam','ebas','ebat','ebamus','ebatis','ebant','iebam','iebas','iebat','iebant']:
        add(v, [base+e])
    # future -am/-es/-et/-emus/-etis/-ent (-iam for -io)
    for e in ['am','es','et','emus','etis','ent','iam','ies','iet','ient']:
        add(v, [base+e])
    # infinitive -ere
    add(v, [base+'ere'])
    # perfect
    for e in ['i','isti','it','imus','istis','erunt','eram','eras','erat','erant']:
        add(v, [perf+e])
    # PPP
    for e in ['us','a','um','i','ae','os','as','o','is','am','e']:
        add(v, [ppp+e])

# 4th-conj: advenio, aperio, audio, dormio, venio
V4 = {'advenio':('adveni','adven','advent'), 'aperio':('aperi','aperu','apert'),
      'audio':('audi','audiv','audit'), 'dormio':('dormi','dormiv','dormit'),
      'venio':('veni','ven','vent')}
for v,(pres,perf,ppp) in V4.items():
    base = pres[:-1]
    for e in ['o','s','t','mus','tis','unt']:
        add(v, [pres+e])
    for e in ['ebam','ebas','ebat','ebamus','ebatis','ebant']:
        add(v, [pres+e])
    for e in ['am','es','et','emus','etis','ent']:
        add(v, [pres+e])
    add(v, [pres+'re'])
    for e in ['i','isti','it','imus','istis','erunt','eram','eras','erat','erant']:
        add(v, [perf+e])
    for e in ['us','a','um','i','ae','os','as','o','is','am','e']:
        add(v, [ppp+e])

# esse
add('sum', ['sum','es','est','sumus','estis','sunt',
            'eram','eras','erat','eramus','eratis','erant',
            'ero','eris','erit','erimus','eritis','erunt',
            'fui','fuisti','fuit','fuimus','fuistis','fuerunt',
            'fueram','fueras','fuerat','fuerant',
            'esse','esset','essent','essem','esses'])
# possum
add('possum', ['possum','potes','potest','possumus','potestis','possunt',
               'poteram','poterat','poterant','poterit','poterunt',
               'potui','potuit','potuerunt','posse','posset','possent'])
# volo
add('volo', ['volo','vis','vult','volumus','vultis','volunt','volebam','volebat','volebant','velle','volui','voluit'])
# coepi / noli
add('coepi', ['coepi','coepit','coeperunt','coepisse'])
add('noli', ['noli','nolite'])
add('necesse', ['necesse'])
# eo
add('eo', ['eo','is','it','imus','itis','eunt','ibam','ibat','ibant','ibo','ibit','ibunt','ii','iit','ierunt','ieram','ierat','ire','iret','iens','euntis'])
add('redeo', ['redeo','redis','redit','redimus','reditis','redeunt','redibam','redibat','redibant','redibit','redibunt','redii','rediit','redierunt','redire','rediret'])
# conatur (deponent)
add('conor', ['conatur','conabatur','conatus'])
# inquit
add('inquit', ['inquit','inquiunt'])

# Nouns (with common declension forms)
NOUNS = {
    'puella': ['puella','puellae','puellam','puellas','puellis','puellarum','puellae'],
    'femina': ['femina','feminae','feminam','feminas','feminis','feminarum'],
    'dea': ['dea','deae','deam','deas','deis','deabus','dearum'],
    'filia': ['filia','filiae','filiam','filias','filiis','filiabus','filiarum'],
    'regina': ['regina','reginae','reginam','reginas','reginis','reginarum'],
    'insula': ['insula','insulae','insulam','insulas','insulis','insularum'],
    'terra': ['terra','terrae','terram','terras','terris','terrarum'],
    'silva': ['silva','silvae','silvam','silvas','silvis','silvarum'],
    'porta': ['porta','portae','portam','portas','portis','portarum'],
    'navis': ['navis','navem','naves','navium','navibus','navi','navi'],
    'urbs': ['urbs','urbis','urbem','urbes','urbium','urbibus','urbi'],
    'pater': ['pater','patris','patrem','patres','patrum','patribus','patri'],
    'deus': ['deus','dei','deo','deum','dei','deos','deorum','dis','diis','deis'],
    'amicus': ['amicus','amici','amico','amicum','amicorum','amicos','amicis'],
    'filius': ['filius','filii','filio','filium','filios','filiorum','filiis','fili'],
    'annus': ['annus','anni','anno','annum','annos','annorum','annis'],
    'cibus': ['cibus','cibi','cibo','cibum','cibos','cibis'],
    'donum': ['donum','doni','dono','dona','donorum','donis'],
    'homo': ['homo','hominis','hominem','homines','hominum','hominibus','homini'],
    'nihil': ['nihil'],
    'vultus': ['vultus','vultum','vultui','vultu'],
    'vir': ['vir','viri','viro','virum','viri','viros','virorum','viris'],
    'iuvenis': ['iuvenis','iuvenem','iuvenes','iuvenum','iuvenibus','iuveni'],
    'maritus': ['maritus','mariti','marito','maritum','maritos'],
    'uxor': ['uxor','uxoris','uxorem','uxores','uxorum','uxoribus'],
    'verbum': ['verbum','verbi','verbo','verba','verbis','verborum'],
    'equus': ['equus','equi','equo','equum','equos','equorum','equis'],
    'caput': ['caput','capitis','capiti','capita','capitibus'],
    'comes': ['comes','comitis','comitem','comites','comitum','comitibus'],
    'consilium': ['consilium','consilii','consilio','consilia','consiliorum','consiliis'],
    'dux': ['dux','ducis','ducem','duces','ducum','ducibus','duci'],
    'gladius': ['gladius','gladii','gladio','gladium','gladios','gladiorum','gladiis'],
    'iter': ['iter','itineris','itinere','itinera','itinerum','itineribus'],
    'manus': ['manus','manum','manui','manu','manuum','manibus'],
    'miles': ['miles','militis','militem','milites','militum','militibus','militi'],
    'mors': ['mors','mortis','mortem','mortes','mortium','mortibus'],
    'rex': ['rex','regis','regem','reges','regum','regibus','regi'],
}
for lem, forms in NOUNS.items():
    add(lem, forms)
add('domum', ['domum','domus','domi','domo'])

# Adjectives
ADJS = {
    'ingens': ['ingens','ingentem','ingentes','ingentis','ingentia','ingentibus','ingenti','ingentium'],
    'laetus': ['laetus','laeta','laetum','laeti','laetae','laetos','laetas','laetis','laetorum','laetarum','laetam','laete'],
    'pulcher': ['pulcher','pulchra','pulchrum','pulchri','pulchrae','pulchros','pulchras','pulchris','pulcherrimus','pulcherrima','pulcherrimum','pulcherrimos'],
    'tristis': ['tristis','triste','tristem','tristes','tristium','tristibus','tristi'],
    'fortis': ['fortis','forte','fortem','fortes','fortium','fortibus','forti','fortior','fortissimus','fortissima','fortissimum','fortissimi','fortissime'],
    'facilis': ['facilis','facile','facilem','faciles','facillimus','facillima','facillimum','facillime'],
    'pauci': ['pauci','paucae','paucos','paucis','paucorum','paucarum','pauca','paucum','paucis'],
    'tantus': ['tantus','tanta','tantum','tanti','tantae','tantos','tantas','tantis','tantam'],
    'iratus': ['iratus','irata','iratum','irati','iratae','iratos','iratas','iratis','iratam'],
    'perterritus': ['perterritus','perterrita','perterritum','perterriti','perterritae','perterritos','perterritas','perterritis','perterritam'],
    'dirus': ['dirus','dira','dirum','diri','dirae','diros','diras','diris','diram','dire'],
    'solus': ['solus','sola','solum','soli','solae','solos','solas','solis','solam'],
    'unus': ['unus','una','unum','uni','unae','unos','unas','unis','unam'],
    'multus': ['multus','multa','multum','multi','multae','multos','multas','multis','multorum','multarum','multam'],
    'omnis': ['omnis','omne','omnem','omnes','omnium','omnibus','omni','omnia'],
    'ceteri': ['ceteri','ceterae','ceteros','ceteras','ceteris','ceterorum','ceterarum'],
    'alius': ['alius','alia','aliud','alii','aliae','alios','alias','aliis','aliam'],
    'bonus': ['bonus','bona','bonum','boni','bonae','bonos','bonas','bonis','bonorum','bonarum','melior','optimus','optima','optimum'],
}
for lem, forms in ADJS.items():
    add(lem, forms)

# Pronouns / demonstratives
add('ego', ['ego','me','mihi','nos','nostri','nostrum','nobis'])
add('tu', ['tu','te','tibi','vos','vestri','vestrum','vobis'])
add('se', ['se','sibi','sui'])
add('suus', ['suus','sua','suum','sui','suae','suos','suas','suis','suam'])
add('ille', ['ille','illa','illud','illum','illam','illi','illae','illo','illis','illos','illas','illorum','illarum'])
add('hic', ['hic','haec','hoc','hunc','hanc','huius','huic','his','horum','harum','hi','hae','haec'])
add('is', ['is','ea','id','eum','eam','eius','ei','eo','eis','eos','eas','eorum','earum'])
add('qui', ['qui','quae','quod','quem','quam','quos','quas','cuius','cui','quo','quibus','quorum','quarum'])

# Preps & particles
for p in ['ad','per','prope','cum','a','ab','e','ex']:
    add(p, [p])
add('in', ['in'])
# Conjunctions / adverbs
FUNCS = ['et','sed','nam','non','etiam','ibi','subito','tam','tum','iterum','nunc','quam','si','tamen','cur','iterum','quod','ubi','deinde','enim','iam','igitur','postquam','simulac','statim','tandem','mox','necesse','quamquam','vix','dum','ut']
for f in FUNCS:
    add(f, [f])
# -que is suffix, handled separately
add('-que', [])

# --- Tokenise and analyse ---
def tokenise(latin):
    s = latin.lower()
    # strip -que suffix as separate token
    toks = re.findall(r"[a-z]+", s)
    out = []
    for t in toks:
        if t.endswith('que') and t != 'que' and len(t) > 3 and t[:-3] in form2lemma:
            out.append(t[:-3]); out.append('-que')
        else:
            out.append(t)
    return out

lemma_first_appearance = {}  # lemma -> (node, set_order_index)
unknowns = {}  # token -> first sentence

# Order sets within a node by their numeric key
for node in sorted(sents):
    node_data = sents[node]
    sorted_sets = sorted(node_data['sets'].keys(), key=lambda x: int(x))
    for si, sk in enumerate(sorted_sets):
        set_data = node_data['sets'][sk]
        for sent in set_data['sentences']:
            for tok in tokenise(sent['latin']):
                if tok in form2lemma:
                    lem = form2lemma[tok]
                    key = (int(node), si)
                    if lem not in lemma_first_appearance or lemma_first_appearance[lem] > key:
                        lemma_first_appearance[lem] = key
                else:
                    if tok not in unknowns:
                        unknowns[tok] = (int(node), sk, sent['latin'])

# Per-node new-lemma lists
by_node = {}
for lem, (node, si) in lemma_first_appearance.items():
    by_node.setdefault(node, []).append(lem)

print('=== PER-NODE FIRST-APPEARANCE LEMMAS ===')
for n in sorted(by_node):
    lems = sorted(by_node[n])
    print(f'\nNode {n} ({len(lems)} new lemmas):')
    print('  ' + ', '.join(lems))

print(f'\n=== UNKNOWN TOKENS ({len(unknowns)}) ===')
for t, (n, sk, ex) in sorted(unknowns.items()):
    print(f'  {t}   (N{n} set{sk}: "{ex}")')

json.dump({
    'per_node': {str(n): sorted(l) for n, l in by_node.items()},
    'unknowns': {t: list(v) for t, v in unknowns.items()}
}, open(P + '_vocab_analysis.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
