// Build CURRICULUM_OVERVIEW.docx — a teacher-editable snapshot of the platform.
// Run: node _build_docs/build_overview.js

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, LevelFormat,
  BorderStyle, WidthType, ShadingType, PageBreak, PageNumber,
  TableOfContents, PageOrientation,
} = require('docx');

// ─────────────────────────────────────────────────────────────────────────
// CONTENT — mirrors current code state as of this build.
// Teacher edits these in Word; developer re-applies to data.py / marking.py.
// ─────────────────────────────────────────────────────────────────────────

const OFFICIAL_GLOSSES = {
  "puella":"girl","dea":"goddess","femina":"woman","pater":"father","filia":"daughter",
  "insula":"island, block of flats","regina":"queen","deus":"god",
  "terra":"land, earth, ground","urbs":"city","navis":"ship","domum":"(to) home",
  "pulcher":"beautiful","tristis":"sad","laetus":"happy","ingens":"huge","multus":"much, many",
  "ego":"I","me":"me","mihi":"to/for me",
  "ille, illa, illud":"he, she, it; that (those)","hic, haec, hoc":"this (these)",
  "in + acc":"into, onto","in + abl":"in, on","ad":"to, towards, at","per":"through",
  "prope":"near","e, ex":"from, out of","a, ab":"(away) from","cum + abl":"with",
  "cum + subj":"when, since","ut + subj":"(so) that, (in order) to",
  "et":"and","sed":"but","nam":"for","-que":"and","non":"not","ibi":"there","tum":"then",
  "subito":"suddenly","etiam":"even, also","tamen":"however","iam":"now, already",
  "nunc":"now","mox":"soon","vix":"hardly, scarcely","statim":"at once, immediately",
  "tandem":"finally, at last","deinde":"then","enim":"for","igitur":"therefore",
  "iterum":"again","quamquam":"although","postquam":"after","dum":"while","si":"if",
  "ubi":"when, where","simulac":"as soon as","cur":"why","quo modo":"how","tam":"so",
  "amo":"I love","rogo":"I ask","habito":"I live","navigo":"I sail","clamo":"I shout",
  "appropinquo":"I approach","impero":"I order","festino":"I hurry","oro":"I beg",
  "oppugno":"I attack","libero":"I free","neco":"I kill","puto":"I think",
  "video; vidi":"I see; I saw","esse(t)":"to be, he/she/it was",
  "est":"(he/she/it/there) is","erat":"(he/she/it/there) was",
  "conspexi":"I noticed","facio; feci":"I make, do; I made, did","habeo":"I have",
  "inquit":"he/she says, said","duco":"I lead","occido":"I kill","advenio":"I arrive",
  "iussi":"I ordered","persuadeo":"I persuade","cognosco":"I get to know, find out",
  "cognovi":"I got to know, found out","dico; dixi":"I say; I said","volo":"I want",
  "dormio":"I sleep","audio":"I hear, listen","pono":"I put, place","posui":"I put, placed",
  "posse(t)":"to be able, he/she/it was able","aperio":"I open",
  "apertus":"(having been) opened","cupio":"I want","peto":"I seek, beg, ask, attack",
  "quaero":"I search, ask (for)","cogo":"I force","coactus":"(having been) forced",
  "appareo":"I appear","redire(t)":"to return, (s)he was returning",
  "rediit":"he/she returned","accepi":"I accepted, received","consilium cepi":"I had an idea",
  "constituo":"I decide","relinquo":"I leave behind","coepi":"I begin","effugio":"I escape",
  "eo":"I leave","discessi":"I left","teneo":"I hold","noli(te)":"don't",
  "conatur":"he/she tries","homo":"man, human","iuvenis":"young (man)","rex":"king",
  "vir":"man","miles":"soldier","dux":"leader","silva":"wood","filius":"son","uxor":"wife",
  "maritus":"husband","comes":"companion","amicus":"friend","equus":"horse","caput":"head",
  "manus":"hand, group","vultus":"face, expression","mors":"death","iter":"journey",
  "gladius":"sword","porta":"gate","cibus":"food","donum":"gift","verbum":"word",
  "annus":"year","iratus":"angry","fortis":"brave, strong","solus":"alone, lonely",
  "dirus":"dreadful","facilis":"easy","omnis":"all, every","unus":"one","pauci":"a few",
  "alius":"other, another","tantus":"so great, such a great","suus":"his, her, its, their",
  "ceteri":"the rest","necesse":"necessary","nihil":"nothing","tu, te":"you (sg)",
  "se":"him-, her-, it(self); them(selves)","eum; eam":"him, it; her, it",
  "eos, eas":"them","ei":"to/for him, her, it","eius":"his, her, its; of him, her, it",
  "qui, quae":"who, which","quod":"because, which","quam":"than, whom, which, how",
};

// Node 1 sentences (Sets 4, 8, 12, 14, 16) — from _node1_new.py
const NODE1_SENTENCES = {
  "Set 4 — Present tense": [
    ["puella deam amat.",
      ["The girl loves the goddess.","The girl is loving the goddess.","The girl likes the goddess.","A girl loves a goddess."],
      ["puella (girl) — nominative singular, subject","deam (goddess) — accusative singular, direct object","amat (loves) — verb, present tense, he/she form"]],
    ["pater filiam rogat.",
      ["The father asks the daughter.","The father asks his daughter.","The father questions the daughter.","The father is asking the daughter."],
      ["pater (father) — nominative singular, subject","filiam (daughter) — accusative singular, direct object","rogat (asks) — verb, present tense, he/she form"]],
    ["femina in insula habitat.",
      ["The woman lives on the island.","The woman is living on the island.","The woman lives in the island.","A woman lives on an island."],
      ["femina (woman) — nominative singular, subject","in insula (on the island) — prepositional phrase: in + ablative = in/on","habitat (lives) — verb, present tense, he/she form"]],
    ["dea pulchra ad terram navigat.",
      ["The beautiful goddess sails towards the land.","The beautiful goddess sails to the land.","The beautiful goddess is sailing towards the land.","A beautiful goddess sails towards the country."],
      ["dea (goddess) — nominative singular, subject","pulchra (beautiful) — adjective, nominative singular feminine, agreeing with dea","ad terram (towards the land) — prepositional phrase: ad + accusative = to/towards","navigat (sails) — verb, present tense, he/she form"]],
    ["regina tristis clamat, nam deus appropinquat.",
      ["The sad queen shouts, for the god approaches.","The sad queen is shouting, for the god is approaching.","The unhappy queen shouts, because the god approaches.","The sad queen shouts, for the god draws near."],
      ["regina (queen) — nominative singular, subject of first clause","tristis (sad) — adjective, nominative singular, agreeing with regina","clamat (shouts) — verb, present tense, he/she form","nam (for) — conjunction introducing a reason","deus (god) — nominative singular, subject of second clause","appropinquat (approaches) — verb, present tense, he/she form"]],
    ["puella laeta patri imperat, et pater festinat.",
      ["The happy girl orders the father, and the father hurries.","The happy girl orders her father, and the father hurries.","The joyful girl orders the father, and the father rushes.","The happy girl is ordering the father, and the father is hurrying."],
      ["puella (girl) — nominative singular, subject of first clause","laeta (happy) — adjective, nominative singular feminine, agreeing with puella","patri (father) — DATIVE singular (impero takes the dative — not 'to the father')","imperat (orders) — verb, present tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","festinat (hurries) — verb, present tense, he/she form"]],
    ["ego feminam oro, sed dea non clamat.",
      ["I beg the woman, but the goddess does not shout.","I beg the woman, but the goddess is not shouting.","I myself beg the woman, but the goddess does not shout.","I plead with the woman, but the goddess does not shout."],
      ["ego (I) — nominative singular, emphatic subject of first clause","feminam (woman) — accusative singular, direct object","oro (I beg) — verb, present tense, I form","sed (but) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","non (not) — negates the verb","clamat (shouts) — verb, present tense, he/she form"]],
    ["multi dei insulam oppugnant, et ibi feminae clamant.",
      ["Many gods attack the island, and there the women shout.","Many gods are attacking the island, and there the women are shouting.","Many of the gods attack the island, and the women are shouting there.","Many gods attack the island, and the women shout there."],
      ["multi (many) — adjective, nominative plural masculine, agreeing with dei","dei (gods) — nominative plural, subject of first clause","insulam (island) — accusative singular, direct object","oppugnant (attack) — verb, present tense, they form","et (and) — coordinating conjunction","ibi (there) — adverb, flexible position in English","feminae (women) — nominative plural, subject of second clause","clamant (shout) — verb, present tense, they form"]],
    ["deus ingens per urbem festinat, et regina puellas liberat.",
      ["The huge god hurries through the city, and the queen frees the girls.","The enormous god hurries through the city, and the queen sets free the girls.","The huge god rushes through the city, and the queen frees the girls.","The vast god is hurrying through the city, and the queen is freeing the girls."],
      ["deus (god) — nominative singular, subject of first clause","ingens (huge) — adjective, nominative singular, agreeing with deus","per urbem (through the city) — prepositional phrase: per + accusative","festinat (hurries) — verb, present tense, he/she form","et (and) — coordinating conjunction","regina (queen) — nominative singular, subject of second clause","puellas (girls) — accusative plural, direct object","liberat (frees) — verb, present tense, he/she form"]],
    ["pater puellam necat, et dea tristis deos orat.",
      ["The father kills the girl, and the sad goddess begs the gods.","The father kills the girl, and the unhappy goddess begs the gods.","The father murders the girl, and the sad goddess pleads with the gods.","The father is killing the girl, and the sad goddess is praying to the gods."],
      ["pater (father) — nominative singular, subject of first clause","puellam (girl) — accusative singular, direct object","necat (kills) — verb, present tense, he/she form","et (and) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","tristis (sad) — adjective agreeing with dea","deos (gods) — accusative plural, direct object","orat (begs) — verb, present tense, he/she form"]],
  ],
  "Set 8 — Imperfect & Future": [
    ["dea clamabat.",
      ["The goddess was shouting.","The goddess used to shout.","The goddess kept shouting.","The goddess shouted."],
      ["dea (goddess) — nominative singular, subject","clamabat (was shouting) — verb, imperfect tense (the -ba- marker), he/she form"]],
    ["pater navigabit.",
      ["The father will sail.","The father will be sailing.","The father is going to sail."],
      ["pater (father) — nominative singular, subject","navigabit (will sail) — verb, future tense (the -bi- marker), he/she form"]],
    ["puella tum clamabat, et pater navigabat.",
      ["The girl was then shouting, and the father was sailing.","Then the girl was shouting, and the father was sailing.","The girl then used to shout, and the father used to sail.","The girl was shouting then, and the father was sailing."],
      ["puella (girl) — nominative singular, subject of first clause","tum (then) — adverb (flexible position in English)","clamabat (was shouting) — verb, imperfect tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","navigabat (was sailing) — verb, imperfect tense, he/she form"]],
    ["regina feminam rogabit, et femina deam orabit.",
      ["The queen will ask the woman, and the woman will beg the goddess.","The queen is going to ask the woman, and the woman is going to beg the goddess.","The queen will question the woman, and the woman will pray to the goddess.","The queen will be asking the woman, and the woman will be begging the goddess."],
      ["regina (queen) — nominative singular, subject of first clause","feminam (woman) — accusative singular, direct object","rogabit (will ask) — verb, future tense, he/she form","et (and) — coordinating conjunction","femina (woman) — nominative singular, subject of second clause","deam (goddess) — accusative singular, direct object","orabit (will beg) — verb, future tense, he/she form"]],
    ["multi dei subito urbem oppugnabant, sed regina in insula habitabat.",
      ["Many gods were suddenly attacking the city, but the queen was living on the island.","Suddenly many gods were attacking the city, but the queen used to live on the island.","Many gods suddenly used to attack the city, but the queen was living on the island.","Many gods were suddenly attacking the city, but the queen lived in the island."],
      ["multi (many) — adjective agreeing with dei","dei (gods) — nominative plural, subject of first clause","subito (suddenly) — adverb (flexible position)","urbem (city) — accusative singular, direct object","oppugnabant (were attacking) — verb, imperfect tense, they form","sed (but) — coordinating conjunction","regina (queen) — nominative singular, subject of second clause","in insula (on the island) — prepositional phrase: in + ablative","habitabat (was living) — verb, imperfect tense, he/she form"]],
    ["puella pulchra in urbem festinabit, et pater clamabit.",
      ["The beautiful girl will hurry into the city, and the father will shout.","The beautiful girl will rush into the city, and the father will shout.","The beautiful girl will be hurrying to the city, and the father will be shouting.","The beautiful girl will hurry to the city, and the father will shout."],
      ["puella (girl) — nominative singular, subject of first clause","pulchra (beautiful) — adjective agreeing with puella","in urbem (into the city) — prepositional phrase: in + accusative = into","festinabit (will hurry) — verb, future tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","clamabit (will shout) — verb, future tense, he/she form"]],
    ["dea me amabat, sed pater tum non orabat.",
      ["The goddess was loving me, but the father was not then begging.","The goddess used to love me, but the father was not begging then.","The goddess loved me, but the father did not beg then.","The goddess was loving me, but my father was not begging then."],
      ["dea (goddess) — nominative singular, subject of first clause","me (me) — accusative singular pronoun, direct object","amabat (was loving) — verb, imperfect tense, he/she form","sed (but) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","tum (then) — adverb (flexible position)","non (not) — negates the verb","orabat (was begging) — verb, imperfect tense, he/she form"]],
    ["dea patrem liberabit, et pater deae tum imperabit.",
      ["The goddess will free the father, and the father will then order the goddess.","The goddess will set free the father, and then the father will order the goddess.","The goddess will free the father, and the father will then order the goddess.","The goddess will free her father, and the father will then order the goddess."],
      ["dea (goddess) — nominative singular, subject of first clause","patrem (father) — accusative singular, direct object","liberabit (will free) — verb, future tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","deae (goddess) — DATIVE singular (impero takes the dative — not 'to the goddess')","tum (then) — adverb (flexible position)","imperabit (will order) — verb, future tense, he/she form"]],
    ["regina illa deum laetum putabat, sed dea non orabat.",
      ["That queen was thinking the god happy, but the goddess was not begging.","That queen thought the god happy, but the goddess was not begging.","That queen used to think the god happy, but the goddess did not beg.","That queen considered the god happy, but the goddess was not praying."],
      ["regina (queen) — nominative singular, subject of first clause","illa (that) — demonstrative agreeing with regina","deum (god) — accusative singular, direct object","laetum (happy) — adjective agreeing with deum — this is the 'double accusative' with puto: 'think X (to be) Y'","putabat (was thinking) — verb, imperfect tense, he/she form","sed (but) — coordinating conjunction","dea (goddess) — nominative singular, new subject","non (not) — negates the verb","orabat (was begging) — verb, imperfect tense, he/she form"]],
    ["ingens navis per terram navigabat, et puella pulchra clamabat.",
      ["A huge ship was sailing through the land, and the beautiful girl was shouting.","An enormous ship was sailing through the land, and the beautiful girl was shouting.","A huge ship used to sail through the land, and the beautiful girl kept shouting.","A huge ship was sailing through the country, and the beautiful girl was shouting."],
      ["ingens (huge) — adjective, nominative singular, agreeing with navis","navis (ship) — nominative singular, subject of first clause","per terram (through the land) — prepositional phrase: per + accusative","navigabat (was sailing) — verb, imperfect tense, he/she form","et (and) — coordinating conjunction","puella (girl) — nominative singular, subject of second clause","pulchra (beautiful) — adjective agreeing with puella","clamabat (was shouting) — verb, imperfect tense, he/she form"]],
  ],
  "Set 12 — Perfect & Pluperfect": [
    ["puella clamavit.",
      ["The girl shouted.","The girl has shouted.","The girl did shout."],
      ["puella (girl) — nominative singular, subject","clamavit (shouted) — verb, perfect tense (the -v- marker), he/she form"]],
    ["pater feminam rogavit.",
      ["The father asked the woman.","The father has asked the woman.","The father questioned the woman.","The father did ask the woman."],
      ["pater (father) — nominative singular, subject","feminam (woman) — accusative singular, direct object","rogavit (asked) — verb, perfect tense, he/she form"]],
    ["dea pulchra deum amavit, et deus clamavit.",
      ["The beautiful goddess loved the god, and the god shouted.","The beautiful goddess has loved the god, and the god has shouted.","The beautiful goddess liked the god, and the god cried out.","The beautiful goddess loved the god, and the god called out."],
      ["dea (goddess) — nominative singular, subject of first clause","pulchra (beautiful) — adjective agreeing with dea","deum (god) — accusative singular, direct object","amavit (loved) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","deus (god) — nominative singular, subject of second clause","clamavit (shouted) — verb, perfect tense, he/she form"]],
    ["regina filiam non liberaverat, sed pater domum festinavit.",
      ["The queen had not freed the daughter, but the father hurried home.","The queen had not set free the daughter, but the father hurried home.","The queen had not freed her daughter, but the father hurried homewards.","The queen had not freed the daughter, but the father has hurried home."],
      ["regina (queen) — nominative singular, subject of first clause","filiam (daughter) — accusative singular, direct object","non (not) — negates the verb","liberaverat (had freed) — verb, pluperfect tense (-verat ending), he/she form","sed (but) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","domum (home) — accusative of motion (no preposition needed)","festinavit (hurried) — verb, perfect tense, he/she form"]],
    ["multi dei ad insulam navigaverunt, et puellas necaverunt.",
      ["Many gods sailed to the island, and killed the girls.","Many gods sailed towards the island, and killed the girls.","Many gods have sailed to the island, and have killed the girls.","Many of the gods sailed to the island, and murdered the girls."],
      ["multi (many) — adjective agreeing with dei","dei (gods) — nominative plural, subject","ad insulam (to the island) — prepositional phrase: ad + accusative","navigaverunt (sailed) — verb, perfect tense, they form","et (and) — coordinating conjunction","puellas (girls) — accusative plural, direct object","necaverunt (killed) — verb, perfect tense, they form"]],
    ["pater ingens puellam amaverat, sed puella tristis deum oraverat.",
      ["The huge father had loved the girl, but the sad girl had begged the god.","The enormous father had loved the girl, but the unhappy girl had begged the god.","The huge father had liked the girl, but the sad girl had pleaded with the god.","The huge father had loved the girl, but the sad girl had prayed to the god."],
      ["pater (father) — nominative singular, subject of first clause","ingens (huge) — adjective agreeing with pater","puellam (girl) — accusative singular, direct object","amaverat (had loved) — verb, pluperfect tense, he/she form","sed (but) — coordinating conjunction","puella (girl) — nominative singular, subject of second clause","tristis (sad) — adjective agreeing with puella","deum (god) — accusative singular, direct object","oraverat (had begged) — verb, pluperfect tense, he/she form"]],
    ["illa dea ad tristem feminam appropinquavit, et clamabat.",
      ["That goddess approached the sad woman, and was shouting.","That goddess drew near to the sad woman, and was shouting.","That goddess came near to the unhappy woman, and kept shouting.","The goddess approached the sad woman, and was shouting."],
      ["illa (that) — demonstrative agreeing with dea","dea (goddess) — nominative singular, subject","ad tristem feminam (to the sad woman) — prepositional phrase: ad + accusative","appropinquavit (approached) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","clamabat (was shouting) — verb, imperfect tense, he/she form"]],
    ["regina urbem oppugnavit, et prope insulam habitavit.",
      ["The queen attacked the city, and lived near the island.","The queen has attacked the city, and has lived near the island.","The queen attacked the city, and dwelt close to the island.","The queen attacked the city, and lived next to the island."],
      ["regina (queen) — nominative singular, subject","urbem (city) — accusative singular, direct object","oppugnavit (attacked) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","prope insulam (near the island) — prepositional phrase: prope + accusative","habitavit (lived) — verb, perfect tense, he/she form"]],
    ["ego deos rogaveram, sed etiam tum non clamaverant.",
      ["I had asked the gods, but even then they had not shouted.","I myself had asked the gods, but still then they had not shouted.","I had asked the gods, but also then they had not shouted.","I had asked the gods, but even at that moment they had not shouted."],
      ["ego (I) — nominative singular, emphatic subject","deos (gods) — accusative plural, direct object","rogaveram (had asked) — verb, pluperfect tense, I form","sed (but) — coordinating conjunction","etiam (even / also / still) — adverb","tum (then) — adverb","non (not) — negates the verb","clamaverant (had shouted) — verb, pluperfect tense, they form (subject = the gods)"]],
    ["pater mihi imperavit, et dea feminam pulchram putaverat.",
      ["The father ordered me, and the goddess had thought the woman beautiful.","The father ordered me, and the goddess had considered the woman beautiful.","The father has ordered me, and the goddess had thought the woman (to be) beautiful.","The father ordered me, and the goddess had thought (that) the woman (was) beautiful."],
      ["pater (father) — nominative singular, subject of first clause","mihi (me) — DATIVE singular pronoun (impero takes the dative — not 'to me')","imperavit (ordered) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","feminam (woman) — accusative singular, direct object","pulchram (beautiful) — adjective agreeing with feminam — 'double accusative' with puto: 'think X (to be) Y'","putaverat (had thought) — verb, pluperfect tense, he/she form"]],
  ],
  "Set 14 — PPP / Passive review": [
    ["puella liberata clamavit.",
      ["The girl, having been freed, shouted.","The freed girl shouted.","The girl who had been freed shouted.","Once freed, the girl shouted."],
      ["puella (girl) — nominative singular, subject","liberata (having been freed) — PPP, nominative singular feminine, agreeing with puella","clamavit (shouted) — verb, perfect tense, he/she form"]],
    ["femina necata erat.",
      ["The woman had been killed.","The woman had been murdered."],
      ["femina (woman) — nominative singular, subject","necata (killed) — PPP, nominative singular feminine, agreeing with femina","erat (had been) — auxiliary forming the pluperfect passive with necata"]],
    ["dea oppugnata ad insulam navigabat.",
      ["The goddess, having been attacked, was sailing to the island.","The goddess, having been attacked, was sailing towards the island.","The attacked goddess was sailing to the island.","The goddess who had been attacked was sailing towards the island."],
      ["dea (goddess) — nominative singular, subject","oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with dea","ad insulam (to the island) — prepositional phrase: ad + accusative","navigabat (was sailing) — verb, imperfect tense, he/she form"]],
    ["pater filiam amatam rogavit.",
      ["The father asked the having-been-loved daughter.","The father asked the daughter who had been loved.","The father asked his beloved daughter.","The father questioned the loved daughter."],
      ["pater (father) — nominative singular, subject","filiam (daughter) — accusative singular, direct object","amatam (having been loved) — PPP, accusative singular feminine, agreeing with filiam","rogavit (asked) — verb, perfect tense, he/she form"]],
    ["regina liberata puellam tristem amavit.",
      ["The queen, having been freed, loved the sad girl.","The freed queen loved the sad girl.","The queen, once freed, loved the unhappy girl.","The queen who had been freed liked the sad girl."],
      ["regina (queen) — nominative singular, subject","liberata (having been freed) — PPP, nominative singular feminine, agreeing with regina","puellam (girl) — accusative singular, direct object","tristem (sad) — adjective, accusative singular, agreeing with puellam","amavit (loved) — verb, perfect tense, he/she form"]],
    ["deus necatus erat, et dea clamabat.",
      ["The god had been killed, and the goddess was shouting.","The god had been murdered, and the goddess kept shouting.","The god had been killed, and the goddess used to shout.","The god had been killed, and the goddess was shouting."],
      ["deus (god) — nominative singular, subject of first clause","necatus (killed) — PPP, nominative singular masculine, agreeing with deus","erat (had been) — auxiliary forming the pluperfect passive with necatus","et (and) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","clamabat (was shouting) — verb, imperfect tense, he/she form"]],
    ["multae feminae oratae erant, sed reginae laetae non festinaverunt.",
      ["Many women had been begged, but the happy queens did not hurry.","Many women had been pleaded with, but the joyful queens did not hurry.","Many women had been prayed to, but the happy queens did not rush.","Many women had been begged, but the happy queens did not hurry."],
      ["multae (many) — adjective agreeing with feminae","feminae (women) — nominative plural, subject of first clause","oratae (begged) — PPP, nominative plural feminine, agreeing with feminae","erant (had been) — auxiliary forming the pluperfect passive with oratae","sed (but) — coordinating conjunction","reginae (queens) — nominative plural, subject of second clause","laetae (happy) — adjective agreeing with reginae","non (not) — negates the verb","festinaverunt (hurried) — verb, perfect tense, they form"]],
    ["puella oppugnata patrem oravit, et pater feminas liberavit.",
      ["The girl, having been attacked, begged the father, and the father freed the women.","The attacked girl begged her father, and the father set free the women.","The girl who had been attacked pleaded with the father, and the father freed the women.","Once attacked, the girl begged the father, and the father freed the women."],
      ["puella (girl) — nominative singular, subject of first clause","oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with puella","patrem (father) — accusative singular, direct object","oravit (begged) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","feminas (women) — accusative plural, direct object","liberavit (freed) — verb, perfect tense, he/she form"]],
    ["dea tristis deum necatum amaverat, sed deus imperatus erat.",
      ["The sad goddess had loved the having-been-killed god, but the god had been ordered.","The sad goddess had loved the killed god, but the god had been commanded.","The unhappy goddess had loved the god who had been killed, but the god had been given orders.","The sad goddess had loved the slain god, but the god had been ordered."],
      ["dea (goddess) — nominative singular, subject of first clause","tristis (sad) — adjective agreeing with dea","deum (god) — accusative singular, direct object","necatum (having been killed) — PPP, accusative singular masculine, agreeing with deum","amaverat (had loved) — verb, pluperfect tense, he/she form","sed (but) — coordinating conjunction","deus (god) — nominative singular, subject of second clause","imperatus (ordered) — PPP, nominative singular masculine, agreeing with deus","erat (had been) — auxiliary forming the pluperfect passive with imperatus"]],
    ["ingens navis oppugnata ad terram navigabat, et multi dei clamaverunt.",
      ["The huge ship, having been attacked, was sailing to the land, and many gods shouted.","The enormous ship, having been attacked, was sailing towards the land, and many gods shouted.","The huge attacked ship was sailing to the land, and many gods shouted.","The vast ship, once attacked, was sailing to the land, and many gods shouted."],
      ["ingens (huge) — adjective agreeing with navis","navis (ship) — nominative singular, subject of first clause","oppugnata (having been attacked) — PPP, nominative singular feminine, agreeing with navis","ad terram (to the land) — prepositional phrase: ad + accusative","navigabat (was sailing) — verb, imperfect tense, he/she form","et (and) — coordinating conjunction","multi (many) — adjective agreeing with dei","dei (gods) — nominative plural, subject of second clause","clamaverunt (shouted) — verb, perfect tense, they form"]],
  ],
  "Set 16 — Exam-level mixed": [
    ["illa puella pulchra reginam oraverat, et dea puellam liberavit.",
      ["That beautiful girl had begged the queen, and the goddess freed the girl.","That beautiful girl had pleaded with the queen, and the goddess set free the girl.","That famous beautiful girl had prayed to the queen, and the goddess freed the girl.","That beautiful girl had begged the queen, and the goddess has freed the girl."],
      ["illa (that) — demonstrative agreeing with puella","puella (girl) — nominative singular, subject of first clause","pulchra (beautiful) — adjective agreeing with puella","reginam (queen) — accusative singular, direct object","oraverat (had begged) — verb, pluperfect tense, he/she form","et (and) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","puellam (girl) — accusative singular, direct object","liberavit (freed) — verb, perfect tense, he/she form"]],
    ["multi dei ad ingentem urbem navigaverunt feminasque necaverunt.",
      ["Many gods sailed to the huge city and killed the women.","Many gods sailed towards the enormous city, and killed the women.","Many of the gods sailed to the huge city and murdered the women.","Many gods sailed to the huge city, and they killed the women."],
      ["multi (many) — adjective agreeing with dei","dei (gods) — nominative plural, subject","ad ingentem urbem (to the huge city) — prepositional phrase: ad + accusative","navigaverunt (sailed) — verb, perfect tense, they form","feminas (women) — accusative plural, direct object","-que (and) — attached to feminas, joining the two verbs","necaverunt (killed) — verb, perfect tense, they form"]],
    ["pater tristis filiam amatam liberaverat, sed dea puellam oppugnavit.",
      ["The sad father had freed the having-been-loved daughter, but the goddess attacked the girl.","The unhappy father had freed the loved daughter, but the goddess attacked the girl.","The sad father had set free his beloved daughter, but the goddess attacked the girl.","The sad father had freed the daughter who had been loved, but the goddess attacked the girl."],
      ["pater (father) — nominative singular, subject of first clause","tristis (sad) — adjective agreeing with pater","filiam (daughter) — accusative singular, direct object","amatam (having been loved) — PPP, accusative singular feminine, agreeing with filiam","liberaverat (had freed) — verb, pluperfect tense, he/she form","sed (but) — coordinating conjunction","dea (goddess) — nominative singular, subject of second clause","puellam (girl) — accusative singular, direct object","oppugnavit (attacked) — verb, perfect tense, he/she form"]],
    ["illa regina tum in insula habitabat, nam dei patrem necaverant.",
      ["That queen was then living on the island, for the gods had killed the father.","That queen used to live on the island then, for the gods had killed the father.","That famous queen was living on the island then, because the gods had killed the father.","That queen was living on the island then, for the gods had killed her father."],
      ["illa (that) — demonstrative agreeing with regina","regina (queen) — nominative singular, subject of first clause","tum (then) — adverb (flexible position)","in insula (on the island) — prepositional phrase: in + ablative","habitabat (was living) — verb, imperfect tense, he/she form","nam (for) — conjunction introducing a reason","dei (gods) — nominative plural, subject of second clause","patrem (father) — accusative singular, direct object","necaverant (had killed) — verb, pluperfect tense, they form"]],
    ["femina pulchra deum rogavit, sed deus illud non putavit.",
      ["The beautiful woman asked the god, but the god did not think that.","The beautiful woman questioned the god, but the god did not think that.","The beautiful woman asked the god, but the god did not believe that.","The beautiful woman asked the god, but the god did not think so."],
      ["femina (woman) — nominative singular, subject of first clause","pulchra (beautiful) — adjective agreeing with femina","deum (god) — accusative singular, direct object","rogavit (asked) — verb, perfect tense, he/she form","sed (but) — coordinating conjunction","deus (god) — nominative singular, subject of second clause","illud (that thing) — neuter demonstrative, accusative, direct object","non (not) — negates the verb","putavit (thought) — verb, perfect tense, he/she form"]],
    ["dea ad terram ingentem navigabat, et puellae oppugnatae clamabant.",
      ["The goddess was sailing to the huge land, and the having-been-attacked girls were shouting.","The goddess was sailing towards the enormous land, and the attacked girls were shouting.","The goddess used to sail to the vast land, and the girls who had been attacked were shouting.","The goddess was sailing to the huge country, and the attacked girls kept shouting."],
      ["dea (goddess) — nominative singular, subject of first clause","ad terram ingentem (to the huge land) — prepositional phrase: ad + accusative; ingentem agrees with terram","navigabat (was sailing) — verb, imperfect tense, he/she form","et (and) — coordinating conjunction","puellae (girls) — nominative plural, subject of second clause","oppugnatae (having been attacked) — PPP, nominative plural feminine, agreeing with puellae","clamabant (were shouting) — verb, imperfect tense, they form"]],
    ["pater ad insulam appropinquavit, et filiam oppugnatam liberavit.",
      ["The father approached to the island, and freed the having-been-attacked daughter.","The father drew near to the island, and freed the attacked daughter.","The father came near to the island, and set free the daughter who had been attacked.","The father approached the island, and freed his attacked daughter."],
      ["pater (father) — nominative singular, subject","ad insulam (to the island) — prepositional phrase: ad + accusative","appropinquavit (approached) — verb, perfect tense, he/she form","et (and) — coordinating conjunction","filiam (daughter) — accusative singular, direct object","oppugnatam (having been attacked) — PPP, accusative singular feminine, agreeing with filiam","liberavit (freed) — verb, perfect tense, he/she form"]],
    ["multi dei reginam tristem oraverant, sed regina deis non imperavit.",
      ["Many gods had begged the sad queen, but the queen did not order the gods.","Many gods had pleaded with the unhappy queen, but the queen did not order the gods.","Many of the gods had prayed to the sad queen, but the queen did not command the gods.","Many gods had begged the sad queen, but the queen has not ordered the gods."],
      ["multi (many) — adjective agreeing with dei","dei (gods) — nominative plural, subject of first clause","reginam (queen) — accusative singular, direct object","tristem (sad) — adjective agreeing with reginam","oraverant (had begged) — verb, pluperfect tense, they form","sed (but) — coordinating conjunction","regina (queen) — nominative singular, subject of second clause","deis (gods) — DATIVE plural (impero takes the dative — not 'to the gods')","non (not) — negates the verb","imperavit (ordered) — verb, perfect tense, he/she form"]],
    ["puella liberata in urbem festinabat, et pater deam tum oravit.",
      ["The girl, having been freed, was hurrying into the city, and the father then begged the goddess.","The freed girl was hurrying into the city, and then the father begged the goddess.","The girl who had been freed was rushing to the city, and the father pleaded with the goddess then.","Once freed, the girl was hurrying into the city, and the father prayed to the goddess then."],
      ["puella (girl) — nominative singular, subject of first clause","liberata (having been freed) — PPP, nominative singular feminine, agreeing with puella","in urbem (into the city) — prepositional phrase: in + accusative = into","festinabat (was hurrying) — verb, imperfect tense, he/she form","et (and) — coordinating conjunction","pater (father) — nominative singular, subject of second clause","deam (goddess) — accusative singular, direct object","tum (then) — adverb (flexible position)","oravit (begged) — verb, perfect tense, he/she form"]],
    ["ille deus pulchras feminas oppugnatas amaverat, sed reginae tristes clamaverant.",
      ["That god had loved the beautiful having-been-attacked women, but the sad queens had shouted.","That god had loved the beautiful attacked women, but the unhappy queens had shouted.","That famous god had liked the beautiful women who had been attacked, but the sad queens had shouted.","That god had loved the beautiful attacked women, but the sad queens had cried out."],
      ["ille (that) — demonstrative agreeing with deus","deus (god) — nominative singular, subject of first clause","pulchras (beautiful) — adjective agreeing with feminas","feminas (women) — accusative plural, direct object","oppugnatas (having been attacked) — PPP, accusative plural feminine, agreeing with feminas","amaverat (had loved) — verb, pluperfect tense, he/she form","sed (but) — coordinating conjunction","reginae (queens) — nominative plural, subject of second clause","tristes (sad) — adjective agreeing with reginae","clamaverant (had shouted) — verb, pluperfect tense, they form"]],
  ],
};

// Node 1 vocab grouped by preview set
const NODE1_VOCAB_GROUPS = [
  ["Set 4 preview — 1st-conj verbs, basic nouns/adjs, core prepositions & conjunctions", [
    ["amo","I love","verb"],["rogo","I ask","verb"],["habito","I live","verb"],
    ["navigo","I sail","verb"],["clamo","I shout","verb"],["appropinquo","I approach","verb"],
    ["impero","I order","verb (+ dative)"],["festino","I hurry","verb"],["oro","I beg","verb"],
    ["oppugno","I attack","verb"],["libero","I free","verb"],["neco","I kill","verb"],
    ["puella","girl","noun"],["dea","goddess","noun"],["femina","woman","noun"],
    ["pater","father","noun"],["filia","daughter","noun"],
    ["insula","island, block of flats","noun"],["regina","queen","noun"],
    ["deus","god","noun"],["terra","land, earth, ground","noun"],["urbs","city","noun"],
    ["pulcher","beautiful","adjective"],["tristis","sad","adjective"],
    ["laetus","happy","adjective"],["ingens","huge","adjective"],
    ["multus","much, many","adjective"],
    ["ego","I","pronoun"],
    ["in + acc","into, onto","preposition"],["in + abl","in, on","preposition"],
    ["ad","to, towards, at","preposition"],["per","through","preposition"],
    ["et","and","conjunction"],["sed","but","conjunction"],["nam","for","conjunction"],
    ["non","not","adverb"],["ibi","there","adverb"],
  ]],
  ["Set 8 preview — puto + demonstrative + adverbs + me", [
    ["puto","I think","verb (+ double accusative)"],
    ["ille, illa, illud","he, she, it; that (those)","demonstrative"],
    ["tum","then","adverb"],["subito","suddenly","adverb"],
    ["me","me","pronoun (acc)"],
  ]],
  ["Set 12 preview — domum, mihi, prope, etiam", [
    ["domum","(to) home","noun (acc of motion)"],
    ["mihi","to/for me","pronoun (dat)"],
    ["prope","near","preposition"],
    ["etiam","even, also","adverb"],
  ]],
  ["Set 14 preview — PPP drill (no new lemmas; uses stems of known verbs)", []],
  ["Set 16 preview — -que, illud", [
    ["-que","and","conjunction (suffix)"],
  ]],
];

// ─────────────────────────────────────────────────────────────────────────
// docx helpers
// ─────────────────────────────────────────────────────────────────────────

const BLACK = "000000";
const NAVY = "1F3A68";
const GREY_BORDER = { style: BorderStyle.SINGLE, size: 4, color: "BFBFBF" };
const BOX_BORDERS = { top: GREY_BORDER, bottom: GREY_BORDER, left: GREY_BORDER, right: GREY_BORDER };

const P = (text, opts = {}) => new Paragraph({
  spacing: { after: 80 },
  ...opts,
  children: Array.isArray(text) ? text : [new TextRun({ text, ...(opts.run || {}) })],
});

const H1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1, pageBreakBefore: true,
  spacing: { before: 240, after: 160 },
  children: [new TextRun({ text, bold: true, size: 36, color: NAVY })],
});
const H2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 },
  children: [new TextRun({ text, bold: true, size: 28, color: NAVY })],
});
const H3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3, spacing: { before: 160, after: 80 },
  children: [new TextRun({ text, bold: true, size: 24, color: BLACK })],
});

const Latin = (text) => new TextRun({ text, italics: true, font: "Cambria" });
const Bold = (text) => new TextRun({ text, bold: true });
const Plain = (text) => new TextRun({ text });

const EditNote = (prompt) => new Paragraph({
  spacing: { before: 60, after: 120 },
  shading: { type: ShadingType.CLEAR, fill: "FFF6D6" },
  border: BOX_BORDERS,
  children: [
    new TextRun({ text: "  ✎ TEACHER EDIT: ", bold: true, color: "8A6200" }),
    new TextRun({ text: prompt, color: "8A6200" }),
    new TextRun({ text: "  " }),
  ],
});

const Bullet = (text, opts = {}) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  spacing: { after: 40 },
  children: Array.isArray(text) ? text : [new TextRun({ text, ...(opts.run || {}) })],
});

const cell = (children, shading, width) => new TableCell({
  borders: { top: GREY_BORDER, bottom: GREY_BORDER, left: GREY_BORDER, right: GREY_BORDER },
  width: { size: width, type: WidthType.DXA },
  shading: shading ? { fill: shading, type: ShadingType.CLEAR } : undefined,
  margins: { top: 80, bottom: 80, left: 120, right: 120 },
  children: Array.isArray(children) ? children : [children],
});

// ─────────────────────────────────────────────────────────────────────────
// Sections
// ─────────────────────────────────────────────────────────────────────────

const children = [];

// ── TITLE ────────────────────────────────────────────────────────────────
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 480, after: 120 },
  children: [new TextRun({ text: "Latin GCSE Mastery Platform", bold: true, size: 48, color: NAVY })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 360 },
  children: [new TextRun({ text: "Curriculum & Design Overview", size: 32, color: NAVY })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 120 },
  children: [new TextRun({ text: "For teacher editing — add your notes, sentences, and corrections directly.", italics: true })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 480 },
  children: [new TextRun({ text: "Eduqas Latin GCSE · Year 11 · Trinity Academy", size: 20, color: "666666" })],
}));

children.push(H2("How to use this document"));
children.push(P("This file is the single place where you can review and mark up everything the platform currently teaches. The developer will read your annotations and apply them to the code."));
children.push(Bullet([
  Bold("Yellow boxes "), Plain("are prompts asking you a specific question — please type your answer inside the box."),
]));
children.push(Bullet([
  Bold("Latin is italicised "), Plain("throughout; English is plain."),
]));
children.push(Bullet([
  Bold("Tracked changes: "), Plain("turn on Review → Track Changes so the developer can see what moved."),
]));
children.push(Bullet([
  Bold("You do not need to touch code. "), Plain("Anything you want changed — sentence wording, a new alternative translation, a vocab gloss, a UI label — just type it into the relevant section."),
]));

// ── 1. Pedagogical architecture ──────────────────────────────────────────
children.push(H1("1 · Pedagogical architecture"));
children.push(P("Content is organised into six progressive nodes. Each node contains a 16-tile grid that mixes (a) teaching panels and (b) sentence practice. The grid is identical in shape for every node, so pupils build a predictable rhythm."));

children.push(H2("The 16-tile grid (applies to every node)"));

const grid = [
  ["1","Teaching","Present — 'I' form (lemma cards)","All new verbs for this node, displayed with principal parts and teacher-approved gloss"],
  ["2","Practice","Present drill","Pupil translates each 1st-person-singular form"],
  ["3","Teaching","Sentence vocabulary","Every non-verb lemma for this node (nouns, adjs, prepositions, conjunctions, adverbs, pronouns)"],
  ["4","Practice","Sentence set 1 — Present","10 sentences, all verbs in present"],
  ["5","Teaching","Imperfect & Future tense endings","Endings table + 'was X-ing / will X' conventions"],
  ["6","Practice","Parse/translate: imperfect & future forms","Short drill on isolated verb forms"],
  ["7","Teaching","(node-specific teaching card)","E.g. double-accusative, PPP, cum + subj, etc."],
  ["8","Practice","Sentence set 2 — Imperfect/Future","10 mixed sentences"],
  ["9","Teaching","Perfect tense — principal parts","-v-, -s-, -u- stems introduced; 3rd PP = perfect stem"],
  ["10","Practice","Parse/translate: perfect forms","Short drill"],
  ["11","Teaching","Pluperfect & exceptions","-verat/-erat patterns + irregulars for this node"],
  ["12","Practice","Sentence set 3 — Perfect/Pluperfect","10 mixed sentences"],
  ["13","Teaching","PPP panel","4th principal part, agreement, passive auxiliaries est/erat/sunt/erant"],
  ["14","Practice","Sentence set 4 — PPP","10 sentences stressing the passive past participle"],
  ["15","Teaching","Exam prep / review","Mixed revision card; no new material"],
  ["16","Practice","Sentence set 5 — Exam-level mixed","10 final sentences, all tenses & structures together"],
];
const gridTable = new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [700, 1100, 2600, 4960],
  rows: [
    new TableRow({
      tableHeader: true,
      children: [
        cell([P("Tile", { run: { bold: true } })], "D5E8F0", 700),
        cell([P("Kind", { run: { bold: true } })], "D5E8F0", 1100),
        cell([P("Title", { run: { bold: true } })], "D5E8F0", 2600),
        cell([P("Content", { run: { bold: true } })], "D5E8F0", 4960),
      ],
    }),
    ...grid.map(row => new TableRow({
      children: row.map((txt, i) => cell([P(txt)], undefined, [700,1100,2600,4960][i])),
    })),
  ],
});
children.push(gridTable);

children.push(EditNote("Do the tile titles read correctly to you? If you would like any renamed, write the new name beside the tile number below:"));
children.push(P("_________________________________________________________________________"));
children.push(P("_________________________________________________________________________"));

// ── 2. The teaching conventions ──────────────────────────────────────────
children.push(H1("2 · Teaching conventions (apply across all nodes)"));

children.push(H2("Verb glossing style"));
children.push(Bullet("Present ideal gloss: 'X-s' (alts add 'is X-ing')"));
children.push(Bullet("Imperfect ideal gloss: 'was X-ing' (alts add 'used to', simple past, 'kept X-ing')"));
children.push(Bullet("Future ideal gloss: 'will X' (alts add 'will be X-ing', 'is going to X')"));
children.push(Bullet("Perfect ideal gloss: 'X-ed' (alts add 'has X-ed', 'did X')"));
children.push(Bullet("Pluperfect ideal gloss: 'had X-ed' (simple past also accepted in compound clauses)"));
children.push(Bullet("PPP strict ideal: 'having been X-ed' (alts: compound adj, post-modifier, relative clause)"));

children.push(H2("Person labels"));
children.push(P([ Plain("The verb explanation bullets say "), Bold("'he/she form'"), Plain(" and "), Bold("'they form'"), Plain(" rather than '3rd singular' and '3rd plural' — this is gentler for Y11 and matches Eduqas mark-scheme wording."), ]));

children.push(H2("Explanation-bullet order"));
children.push(P("Each sentence comes with a bullet list explaining every lemma. Bullets are ordered by English reading order (Subject → Verb → Object), NOT Latin left-to-right order. This stops pupils being told to read Latin word-for-word."));
children.push(EditNote("Do you want any sentence's bullets re-ordered? Mark the sentence number and write the new order."));

children.push(H2("Double-accusative verbs"));
children.push(P([ Latin("puto"), Plain(" takes a double accusative: 'I think X (to be) Y'. The bullet for the second accusative explicitly flags this."), ]));

children.push(H2("Impero + dative"));
children.push(P([ Latin("impero"), Plain(" takes the dative. The bullet warns: 'DATIVE singular (impero takes the dative — not \"to the father\")'."), ]));

children.push(H2("PPP + est/erat/sunt/erant"));
children.push(P("When a PPP appears with a form of sum, it forms the perfect/pluperfect passive ('had been X-ed'). The explanation bullet flags the auxiliary explicitly."));
children.push(EditNote("Happy with how PPP + sum is explained in Set 14? If any bullet is unclear, mark the sentence number."));

// ── 3. Marking flexibility ──────────────────────────────────────────────
children.push(H1("3 · Marking flexibility"));
children.push(P("The marking engine accepts more than just the 'ideal' answer. A translation is judged correct if it matches ANY of these after normalisation:"));

const flex = [
  ["Articles", "'the', 'a', 'an' — freely inserted or omitted"],
  ["Possessives", "'his', 'her', 'their' may be inserted before relational nouns (father → his father, daughter → her daughter)"],
  ["Punctuation", "Trailing punctuation and extra commas are ignored"],
  ["Tense synonyms", "Progressive ↔ simple (was X-ing ↔ X-ed); 'used to'; 'kept'; 'did X' (emphatic)"],
  ["Motion-verb 'to'", "approached/came/went/arrived/hurried/rushed/sailed/ran/returned — 'to' or 'towards' may be dropped after them"],
  ["Pluperfect drop", "'had X-ed' ↔ 'X-ed' in compound sentences"],
  ["PPP placement", "'having been X-ed noun' ↔ 'X-ed noun' ↔ 'noun who had been X-ed' ↔ 'noun, having been X-ed'"],
  ["Preposition synonyms", "ad + acc: 'to' ↔ 'towards'; in + acc: 'into' ↔ 'to' (motion); in + abl: 'in' ↔ 'on' (context)"],
  ["Adverb placement", "tum, ibi, subito, etiam may sit before or after the verb"],
  ["Typo tolerance", "Levenshtein distance ≤ 1 on words > 4 chars"],
  ["Top-150 synonym pool", "e.g. love ↔ like; attack ↔ assault; shout ↔ cry out; beautiful ↔ lovely; etc."],
];
const flexTable = new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [2400, 6960],
  rows: [
    new TableRow({
      tableHeader: true,
      children: [
        cell([P("Feature", { run: { bold: true } })], "D5E8F0", 2400),
        cell([P("What we accept", { run: { bold: true } })], "D5E8F0", 6960),
      ],
    }),
    ...flex.map(r => new TableRow({
      children: [cell([P(r[0])], undefined, 2400), cell([P(r[1])], undefined, 6960)],
    })),
  ],
});
children.push(flexTable);

children.push(H2("Near-miss feedback"));
children.push(P("If a pupil's answer is very close but wrong in exactly one way, the marking engine says:"));
children.push(Bullet([ Bold("Tense error: "), Plain("\"Close! You misidentified the tense of the verb. (Should be X, not Y.) The answer is: ...\"") ]));
children.push(Bullet([ Bold("Number error: "), Plain("\"Nearly! You need to make sure what's singular versus plural.\"") ]));
children.push(Bullet([ Bold("Person error: "), Plain("\"Nearly — check who's doing the action.\"") ]));
children.push(P("All three are still counted WRONG; the label just tells the pupil where to look."));

children.push(EditNote("Any other single-error patterns you'd like flagged? E.g. case confusion, dative vs. accusative, etc. — write here:"));
children.push(P("_________________________________________________________________________"));

// ── 4. Official vocab index ─────────────────────────────────────────────
children.push(H1("4 · Official vocabulary index"));
children.push(P("Every gloss the platform shows pupils is pulled verbatim from this list. Nothing here is paraphrased from Lewis & Short, Perseus, or any online dictionary. If a word needs an extra sense, add it below and the developer will mirror it in the code's OFFICIAL_GLOSSES file."));

const glossEntries = Object.entries(OFFICIAL_GLOSSES);
const glossRows = [];
glossRows.push(new TableRow({
  tableHeader: true,
  children: [
    cell([P("Latin lemma (as shown on card)", { run: { bold: true } })], "D5E8F0", 3600),
    cell([P("Teacher-authoritative English gloss", { run: { bold: true } })], "D5E8F0", 5760),
  ],
}));
for (const [lemma, gloss] of glossEntries) {
  glossRows.push(new TableRow({ children: [
    cell([new Paragraph({ children: [Latin(lemma)] })], undefined, 3600),
    cell([P(gloss)], undefined, 5760),
  ]}));
}
children.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [3600, 5760],
  rows: glossRows,
}));
children.push(EditNote("Add or amend any gloss above — either by tracked-changes edit of the cell, or by listing corrections here:"));
children.push(P("_________________________________________________________________________"));
children.push(P("_________________________________________________________________________"));

// ── 5. Node 1 full content ──────────────────────────────────────────────
children.push(H1("5 · Node 1 — full content (complete and in production)"));
children.push(P("This is the only node where every sentence, bullet, and vocab card is finalised. Use it as the gold standard when reviewing Nodes 2–6."));

children.push(H2("Node 1 vocabulary — grouped by preview set"));
for (const [groupTitle, items] of NODE1_VOCAB_GROUPS) {
  children.push(H3(groupTitle));
  if (items.length === 0) {
    children.push(P("(No new lemmas — form-drill only.)", { run: { italics: true } }));
    continue;
  }
  const rows = [new TableRow({
    tableHeader: true,
    children: [
      cell([P("Latin", { run: { bold: true } })], "D5E8F0", 2400),
      cell([P("Gloss", { run: { bold: true } })], "D5E8F0", 4400),
      cell([P("Part of speech", { run: { bold: true } })], "D5E8F0", 2560),
    ],
  })];
  for (const [lat, eng, pos] of items) {
    rows.push(new TableRow({ children: [
      cell([new Paragraph({ children: [Latin(lat)] })], undefined, 2400),
      cell([P(eng)], undefined, 4400),
      cell([P(pos)], undefined, 2560),
    ]}));
  }
  children.push(new Table({ width: { size: 9360, type: WidthType.DXA }, columnWidths: [2400,4400,2560], rows }));
}

children.push(H2("Node 1 sentences — full detail"));
children.push(P("Each sentence block below shows:"));
children.push(Bullet("The Latin sentence."));
children.push(Bullet("The 'ideal' translation (first row, shaded blue) — this is what the system shows as the model answer."));
children.push(Bullet("The accepted alternative translations (also counted correct)."));
children.push(Bullet("The explanation bullets shown after the pupil submits."));

let sentenceIndex = 0;
for (const [setTitle, sents] of Object.entries(NODE1_SENTENCES)) {
  children.push(H3(setTitle));
  for (const [latin, englishes, bullets] of sents) {
    sentenceIndex++;
    children.push(new Paragraph({
      spacing: { before: 200, after: 80 },
      children: [
        new TextRun({ text: `Sentence ${sentenceIndex}  · ` , bold: true, color: NAVY }),
        Latin(latin),
      ],
    }));

    // translations table
    const trRows = [];
    trRows.push(new TableRow({
      tableHeader: true,
      children: [
        cell([P("", { run: { bold: true } })], "D5E8F0", 1200),
        cell([P("Accepted English translation", { run: { bold: true } })], "D5E8F0", 8160),
      ],
    }));
    englishes.forEach((eng, i) => {
      trRows.push(new TableRow({ children: [
        cell([P(i === 0 ? "Ideal" : `Alt ${i}`, { run: { bold: i===0 } })], i===0 ? "EAF4FB" : undefined, 1200),
        cell([P(eng)], i===0 ? "EAF4FB" : undefined, 8160),
      ]}));
    });
    children.push(new Table({ width: { size: 9360, type: WidthType.DXA }, columnWidths: [1200,8160], rows: trRows }));

    children.push(new Paragraph({
      spacing: { before: 80, after: 40 },
      children: [new TextRun({ text: "Explanation bullets (shown after submission, in English reading order):", bold: true, size: 20 })],
    }));
    for (const b of bullets) {
      children.push(Bullet(b));
    }
    children.push(EditNote(`Sentence ${sentenceIndex}: any corrections to the Latin, the ideal, the alternatives, or the bullets?`));
  }
}

// ── 6. Placeholder for Nodes 2–6 ────────────────────────────────────────
for (let n = 2; n <= 6; n++) {
  children.push(H1(`6.${n - 1} · Node ${n} — NOT YET REWRITTEN (skeleton for teacher input)`));
  children.push(P(`Node ${n} still contains the old content in the code. Below is the skeleton the developer needs before rewriting. Please fill in each section — sentences especially. Even rough drafts are useful; the developer can polish the wording.`));

  const nodeHints = {
    2: "New lemmas expected: homo, iuvenis, rex, vir, miles, dux, silva, filius; cum + abl; iratus; fortis; new pronouns tu/te; eum/eam; qui/quae. Grammar focus: 3rd-declension nouns, cum + ablative, relative pronoun introduction.",
    3: "New lemmas expected: uxor, maritus, comes, amicus, equus, caput, manus, vultus, mors, iter, gladius, porta, cibus, donum, verbum, annus; solus, dirus, facilis, omnis, unus, pauci, alius, tantus. Grammar focus: 2nd-conjugation verbs (video, habeo, teneo), reflexive se.",
    4: "New lemmas expected: suus, ceteri, necesse, nihil; eos/eas, ei, eius; quod, quam; ubi, simulac, cur, quo modo. Grammar focus: 3rd/4th-conjugation verbs (duco, occido, advenio, audio, dormio, pono), purpose clauses with ut + subj.",
    5: "New lemmas expected: tam, tamen, iam, nunc, mox, vix, statim, tandem, deinde, enim, igitur, iterum; est, erat, esse(t), posse(t); quamquam, postquam, dum, si. Grammar focus: esse and posse (irregulars), subordinating conjunctions, conditional si.",
    6: "New lemmas expected: inquit, aperio/apertus, cupio, peto, quaero, cogo/coactus, appareo, redire(t)/rediit, accepi, consilium cepi, constituo, relinquo, coepi, effugio, eo/discessi, noli(te), conatur. Grammar focus: irregulars, indirect statement, exam-style mixed.",
  };
  children.push(P(nodeHints[n]));

  children.push(H2(`Node ${n} — vocabulary (proposed)`));
  const vocabTable = new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2400,4400,2560],
    rows: [
      new TableRow({
        tableHeader: true,
        children: [
          cell([P("Latin lemma", { run: { bold: true } })], "D5E8F0", 2400),
          cell([P("Gloss (from official word list)", { run: { bold: true } })], "D5E8F0", 4400),
          cell([P("Preview-set placement (4 / 8 / 12 / 14 / 16)", { run: { bold: true } })], "D5E8F0", 2560),
        ],
      }),
      ...Array.from({ length: 12 }, () => new TableRow({ children: [
        cell([P(" ")], undefined, 2400),
        cell([P(" ")], undefined, 4400),
        cell([P(" ")], undefined, 2560),
      ]})),
    ],
  });
  children.push(vocabTable);
  children.push(EditNote(`Node ${n}: please list any additional lemmas you want introduced here, and where each should sit (which preview set).`));

  for (const setName of ["Set 4 — Present", "Set 8 — Imperfect/Future", "Set 12 — Perfect/Pluperfect", "Set 14 — PPP", "Set 16 — Exam-level mixed"]) {
    children.push(H2(`Node ${n} — ${setName}`));
    children.push(P("Sketch 10 sentences for this set. The developer will write explanation bullets in English reading order once you approve the Latin and translations."));
    const sentBox = new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [500, 3800, 5060],
      rows: [
        new TableRow({
          tableHeader: true,
          children: [
            cell([P("#", { run: { bold: true } })], "D5E8F0", 500),
            cell([P("Latin", { run: { bold: true } })], "D5E8F0", 3800),
            cell([P("Ideal English translation + any alternatives you'd accept", { run: { bold: true } })], "D5E8F0", 5060),
          ],
        }),
        ...Array.from({ length: 10 }, (_, i) => new TableRow({ children: [
          cell([P(String(i+1))], undefined, 500),
          cell([P(" ")], undefined, 3800),
          cell([P(" ")], undefined, 5060),
        ]})),
      ],
    });
    children.push(sentBox);
  }
}

// ── 7. UI / teaching-panel notes ────────────────────────────────────────
children.push(H1("7 · UI and teaching-panel notes"));
children.push(H2("Vocab-card colour coding"));
children.push(Bullet("Teal pill — preposition"));
children.push(Bullet("Purple pill — pronoun"));
children.push(Bullet("Amber pill — demonstrative"));
children.push(Bullet("Grey pill — conjunction/adverb"));
children.push(Bullet("Blue pill — verb (shows principal parts on hover)"));
children.push(Bullet("Green pill — noun (gender + declension on hover)"));
children.push(Bullet("Orange pill — adjective"));
children.push(EditNote("Do you want the colour/label mapping changed for any category?"));

children.push(H2("Latin font"));
children.push(P("All Latin on the site (card faces, sentence prompts, model answers) should render in the Cambria serif family so it's visually distinct from the surrounding English sans-serif UI."));

children.push(H2("Explanation panel — ordering rule"));
children.push(P("Bullets render after submission, below the model answer. They use English reading order (Subject → Verb → Object). Latin-left-to-right order is explicitly avoided."));

children.push(H2("Duplicate-explanation bug (reported)"));
children.push(P("On some sentences the explanation block rendered twice. Fix scheduled. If you see it elsewhere, note the sentence below."));
children.push(EditNote("Record any remaining duplicate-explanation sightings (node + set + sentence #):"));

children.push(H2("Future-tense teaching table (reported bug)"));
children.push(P("The future-tense key/legend styling is currently broken. Fix scheduled."));

children.push(H2("PPP teaching panel"));
children.push(P("The PPP panel needs a -v- highlight on the 3rd principal part (perfect stem) so pupils see where the PPP stem differs from the perfect stem. Plus a short note that est/erat/sunt/erant combine with a PPP to make the passive."));

// ── 8. Developer hand-off ──────────────────────────────────────────────
children.push(H1("8 · Hand-off instructions for the developer"));
children.push(P("When this document comes back with teacher edits, apply changes in the following order to avoid churn:"));
children.push(Bullet("Section 4 (Official glosses): update y11/OFFICIAL_GLOSSES.py."));
children.push(Bullet("Section 5 (Node 1 sentences): update y11/data.py Node 1 sentence lists and explanation bullets."));
children.push(Bullet("Sections 6.1–6.5 (Nodes 2–6): compose new _node2_new.py … _node6_new.py files following the Node 1 template, then splice into data.py."));
children.push(Bullet("Section 3 (Marking flexibility): update marking.py if new near-miss patterns are requested."));
children.push(Bullet("Section 7 (UI): apply to the React front-end."));
children.push(P("After each round of edits, re-generate this document from the updated data so the teacher can review changes in context."));

// Closing
children.push(new Paragraph({
  spacing: { before: 480 },
  alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "— End of document —", italics: true, color: "888888" })],
}));

// ─────────────────────────────────────────────────────────────────────────
// Document assembly
// ─────────────────────────────────────────────────────────────────────────

const doc = new Document({
  creator: "Latin GCSE Platform",
  title: "Latin GCSE Curriculum & Design Overview",
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Calibri", color: NAVY },
        paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Calibri", color: NAVY },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Calibri" },
        paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
      },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Latin GCSE Mastery — Curriculum Overview", size: 18, color: "888888" })],
      })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Page ", size: 18, color: "888888" }),
          new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "888888" }),
          new TextRun({ text: " of ", size: 18, color: "888888" }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 18, color: "888888" }),
        ],
      })] }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buffer => {
  const out = path.resolve("C:/Users/mmhun/Desktop/y11_latin_gcse/CURRICULUM_OVERVIEW.docx");
  fs.writeFileSync(out, buffer);
  console.log("Wrote " + out + "  (" + buffer.length + " bytes)");
}).catch(err => {
  console.error(err);
  process.exit(1);
});
