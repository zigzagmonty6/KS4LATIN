import json

raw_text = """erat	(he/she/it/there) was	tam	so	homo	man, human
in + acc	into, onto	terra	land, earth, ground	igitur	therefore
in + abl	in, on	est	(he/she/it/there) is	ingens	huge
ut + subj	(so) that, (in order) to	me	me	iterum	again
eum; eam	him, it; her, it	festino	I hurry	iuvenis	young (man)
ad	to, towards, at	a, ab	(away) from	mors	death
qui, quae	who, which	annus	year	nam	for
deus	god	cum + abl	with	necesse	necessary
non	not	iter	journey	omnis	all, every
ille, illa, illud	he, she, it; that (those)	laetus	happy	pauci	a few
et	and	mox	soon	quam	than, whom, which, how
quod	because, which	navis	ship	si	if
multus	much, many	perterritus	terrified	unus	one
sed	but	puella	girl	verbum	word
hic, haec, hoc	this (these)	rex	king	vix	hardly, scarcely
dea	goddess	silva	wood	noli(te)	don’t
ei	to/for him, her, it 	urbs	city	discedo	I leave
video; vidi	I see; I saw	neco	I kill	discessi	I left
esse(t)	to be, he/she/it was	navigo	I sail	teneo	I hold
conspexi	I noticed	aperio	I open	amo	I love
facio; feci	I make, do; I made, did	apertus	(having been) opened	effugio	I escape
rogo	I ask	cupio	I want	libero	I free
tu, te	you (sg)	puto	I think	peto	I seek, beg, ask, attack
ubi	when, where	cibus	food	quaero	I search, ask (for)
vir	man	comes	companion	cogo	I force
habeo	I have	facilis	easy	coactus	(having been) forced
inquit	he/she says, said	femina	woman	appareo	I appear
e, ex	from, out of	fortis	brave, strong	appropinquo	I approach
per	through	suus	his, her, its, their	clamo	I shout
-que	and	tantus	so great, such a great	impero	I order
tamen	however	dormio	I sleep	pono	I put, place
uxor	wife	audio	I hear, listen	posui	I put, placed
eius	his, her, its; of him, her, it	duco	I lead	oppugno	I attack
posse(t)	to be able, he/she/it was able	occido	I kill	amicus	friend
caput	head	advenio	I arrive	cur	why
pulcher	beautiful	iussi	I ordered	dirus	dreadful
se	him-, her-, it(self); them(selves)	persuadeo	I persuade	dum	while
simulac	as soon as	cognosco	I get to know, find out	dux	leader
dico; dixi	I say; I said	cognovi	I got to know, found out	etiam	even, also
volo	I want	conatur	he/she tries	filia	daughter
cum + subj	when, since	alius	other, another	gladius	sword
equus	horse	domum	(to) home	iam	now, already
iratus	angry	ibi	there	maritus	husband
postquam	after	manus	hand, group	nihil	nothing
statim	at once, immediately	regina	queen	nunc	now
tandem	finally, at last	eos, eas	them	porta	gate
redire(t)	to return, (s)he was returning	habito	I live	prope	near
rediit	he/she returned	oro	I beg	quo modo	how
deinde	then	accepi	I accepted, received	solus	alone, lonely
ego	I	consilium cepi	I had an idea	subito	suddenly
enim	for	constituo	I decide	tristis	sad
filius	son	relinquo	I leave behind	tum	then
miles	soldier	ceteri	the rest	vultus	face, expression
pater	father	donum	gift	mihi	to/for me
quamquam	although	insula	island, block of flats	coepi	I begin"""

vocab_dict = {}
lines = raw_text.split('\n')
for line in lines:
    parts = line.strip().split('\t')
    for i in range(0, len(parts)-1, 2):
        lat = parts[i].strip()
        eng = parts[i+1].strip()
        if lat and eng:
            vocab_dict[lat] = eng

with open('reference_bank.py', 'w', encoding='utf-8') as f:
    f.write("# reference_bank.py\n")
    f.write("# Exact English definitions as prescribed by the Top 150 document.\n\n")
    f.write("TOP_150_BANK = {\n")
    for lat, eng in vocab_dict.items():
        f.write(f'    "{lat}": "{eng}",\n')
    f.write("}\n")
