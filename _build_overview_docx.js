// Build CURRICULUM_OVERVIEW.docx — editable teacher overview.
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, PageOrientation,
  HeadingLevel, BorderStyle, WidthType, ShadingType, PageNumber, PageBreak
} = require('docx');

const BORDER = { style: BorderStyle.SINGLE, size: 4, color: "BFBFBF" };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const HEADER_SHADE = { fill: "D9E7F5", type: ShadingType.CLEAR, color: "auto" };
const EDIT_SHADE   = { fill: "FFF9E6", type: ShadingType.CLEAR, color: "auto" };  // yellow = editable
const NOTE_SHADE   = { fill: "F0F0F0", type: ShadingType.CLEAR, color: "auto" };
const CELL_MARGINS = { top: 80, bottom: 80, left: 120, right: 120 };

// US Letter portrait content width = 12240 - 1440*2 = 9360 DXA
const CONTENT_W = 9360;

function P(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 },
    ...opts,
    children: [new TextRun({ text, ...(opts.run || {}) })],
  });
}
function PR(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 120 }, ...opts, children: runs });
}
function H(text, level) {
  return new Paragraph({
    heading: level,
    spacing: { before: 240, after: 120 },
    children: [new TextRun({ text })],
  });
}
function bullet(text, run = {}) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: [new TextRun({ text, ...run })],
  });
}
function cell(children, { width, shading, bold } = {}) {
  const paras = (Array.isArray(children) ? children : [children]).map(c =>
    typeof c === 'string'
      ? new Paragraph({ children: [new TextRun({ text: c, bold: !!bold })] })
      : c
  );
  return new TableCell({
    borders: BORDERS,
    margins: CELL_MARGINS,
    width: { size: width, type: WidthType.DXA },
    shading: shading || undefined,
    children: paras.length ? paras : [new Paragraph({ children: [new TextRun("")] })],
  });
}
function headerRow(labels, widths) {
  return new TableRow({
    tableHeader: true,
    children: labels.map((l, i) => cell(l, { width: widths[i], shading: HEADER_SHADE, bold: true })),
  });
}
function dataRow(vals, widths, { editable } = {}) {
  return new TableRow({
    children: vals.map((v, i) => cell(v || "", { width: widths[i], shading: editable ? EDIT_SHADE : undefined })),
  });
}
function makeTable(rows, widths) {
  return new Table({
    width: { size: widths.reduce((a,b)=>a+b,0), type: WidthType.DXA },
    columnWidths: widths,
    rows,
  });
}
function teacherNoteRow(widths) {
  // A single merged-feel row for teacher annotation (we just use one wide cell spanning by using total width)
  const total = widths.reduce((a,b)=>a+b,0);
  return new TableRow({
    children: [new TableCell({
      borders: BORDERS,
      margins: CELL_MARGINS,
      width: { size: total, type: WidthType.DXA },
      columnSpan: widths.length,
      shading: NOTE_SHADE,
      children: [new Paragraph({ children: [new TextRun({ text: "Teacher notes: ", bold: true, italics: true, color: "666666" })] })],
    })],
  });
}

// ---------- CONTENT ----------

const children = [];

// Title page
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 240 },
  children: [new TextRun({ text: "Latin GCSE Mastery Platform", bold: true, size: 48 })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 120 },
  children: [new TextRun({ text: "Curriculum & Design Overview", size: 32 })],
}));
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { after: 480 },
  children: [new TextRun({ text: "For teacher editing — annotate, then hand back to developer", italics: true, size: 22, color: "666666" })],
}));

// How to use
children.push(H("How to use this document", HeadingLevel.HEADING_1));
children.push(P("This document mirrors the content and behaviour currently in the platform. It is designed to be marked up directly in Word."));
children.push(bullet("Cells shaded pale yellow are editable content (sentences, translations, vocab glosses). Cross out, rewrite, or use tracked changes."));
children.push(bullet("Grey \"Teacher notes\" rows sit under each table — use them to leave free-text instructions for the developer."));
children.push(bullet("To add/remove an entire sentence or vocab item, just strike the whole row or add a new row underneath."));
children.push(bullet("The \"Valid translations\" and \"Marking behaviour\" section at the end captures accept/reject rules — edit these to adjust leniency."));
children.push(bullet("For UI wording, font-colour scheme, and banner text, see the \"UI & Design Conventions\" section."));

// Platform design
children.push(H("Platform architecture (reference)", HeadingLevel.HEADING_1));
children.push(bullet("Backend: FastAPI (y11/app.py) + SQLite pupil database"));
children.push(bullet("Frontend: single-file React SPA in y11/static/index.html (no build step)"));
children.push(bullet("Content authoring: y11/data.py (all sets, sentences, vocab, tables)"));
children.push(bullet("Marking & equivalence: y11/marking.py"));
children.push(bullet("Canonical glosses: y11/OFFICIAL_GLOSSES.py"));
children.push(bullet("Specification: Eduqas GCSE Latin, Y11, Trinity Academy"));

// UI & Design conventions
children.push(H("UI & Design conventions", HeadingLevel.HEADING_1));

children.push(H("Font-colour scheme for Latin forms", HeadingLevel.HEADING_2));
children.push(P("Default text colour is BLACK. Specific morphological elements are coloured solid (no underline, no bold mixing):"));
const colourRows = [
  headerRow(["Element", "Colour", "Example (in principal parts: amo, amare, amavi, amatus)"], [2000, 2000, 5360]),
  dataRow(["Person ending  (-o, -s, -t, -mus, -tis, -nt)", "Blue", "am-O,  ama-S,  ama-T,  ama-MUS …"], [2000, 2000, 5360]),
  dataRow(["Stem vowel  (the conjugation vowel)", "Red",  "am-A-re,  am-A-vi,  am-A-tus"], [2000, 2000, 5360]),
  dataRow(["Tense marker (-ba-, -bo/-bi/-bu-, -v-, -u-, -s-, -era-)", "Purple", "ama-BA-t,  ama-V-i,  ama-V-eram"], [2000, 2000, 5360]),
  dataRow(["Infinitive ending  (-re)", "Green",  "ama-RE,  vide-RE,  dice-RE"], [2000, 2000, 5360]),
  dataRow(["PPP ending  (-tus / -sus)", "Yellow", "ama-TUS,  vis-US,  duc-TUS"], [2000, 2000, 5360]),
  dataRow(["Everything else", "Black (default)", "am, vid, duc, reg …"], [2000, 2000, 5360]),
  teacherNoteRow([2000, 2000, 5360]),
];
children.push(makeTable(colourRows, [2000, 2000, 5360]));
children.push(P(""));
children.push(P("Platform does NOT display vowel-length macrons.", { run: { italics: true, color: "666666" } }));

children.push(H("Wrong-answer message bank", HeadingLevel.HEADING_2));
children.push(P("When a pupil gets a sentence wrong with no specific near-miss hint available, one of these is shown at random (no em-dashes):"));
["Unlucky! Take another look at this one.",
 "Whoops! Something's gone wrong here.",
 "Wrong! Give it another go.",
 "Incorrect! Latin is all about precision.",
 "Oh no! Something needs fixing."].forEach(m => children.push(bullet(m)));
children.push(PR([new TextRun({ text: "Teacher notes: ", bold: true, italics: true, color: "666666" })]));

children.push(H("Banner & label wording", HeadingLevel.HEADING_2));
const uiRows = [
  headerRow(["Location", "Current wording", "Edit here"], [2800, 3280, 3280]),
  dataRow(["Green banner (success)", "Correct!", ""], [2800, 3280, 3280], { editable: false }),
  dataRow(["Retype banner on re-attempt", "Try this again! You got it wrong before.", ""], [2800, 3280, 3280], { editable: true }),
  dataRow(["Retype prompt", "Type the correct answer to continue:", ""], [2800, 3280, 3280], { editable: true }),
  dataRow(["Reveal label", "The correct answer is", ""], [2800, 3280, 3280], { editable: true }),
  dataRow(["Vocab partial-meaning hint", "Close! You need to list all its meanings: …", ""], [2800, 3280, 3280], { editable: true }),
  teacherNoteRow([2800, 3280, 3280]),
];
children.push(makeTable(uiRows, [2800, 3280, 3280]));

children.push(H("Near-miss hint types (automatic)", HeadingLevel.HEADING_2));
children.push(bullet("Tense error (e.g. \"loved\" for \"loves\") — rejects with hint, does not silently accept."));
children.push(bullet("Number error (sg vs pl, e.g. \"you (sg)\" vs \"you (pl)\")."));
children.push(bullet("Person error (1st/2nd/3rd)."));
children.push(bullet("\"in\" vs \"into\" (preposition +ABL vs +ACC)."));
children.push(bullet("Missing one of several required meanings."));
children.push(bullet("Typos (Levenshtein distance 1) — accepted with advisory, not rejected."));
children.push(bullet("Punctuation-only differences — silently accepted, no advisory."));

// ---------- CURRICULUM NODES ----------
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Curriculum — by Node", HeadingLevel.HEADING_1));
children.push(P("Each Node has ~13–16 sets. The tables below list every sentence translation set and vocab list that the teacher authors. Rewrite English translations directly in the yellow cells; add \"also accept:\" alternatives in the rightmost column.", { run: { italics: true, color: "666666" } }));

// ---- NODE 1 ----
children.push(H("Node 1 — 1st Conjugation (Top 150)", HeadingLevel.HEADING_2));
children.push(P("Sets: Present I-form → Present endings → Present sentences → Infinitive → Imperfect → Future → Present-system sentences → Perfect I-form → Perfect endings → Pluperfect → Active sentences → PPP → PPP sentences → Build-principal-parts → Review."));

function sentenceTable(title, rows) {
  children.push(H(title, HeadingLevel.HEADING_3));
  const widths = [520, 2720, 3200, 2920];
  const trs = [headerRow(["#", "Latin", "Canonical English", "Also accept / notes"], widths)];
  rows.forEach((r, i) => trs.push(dataRow([String(i+1), r[0], r[1], r[2] || ""], widths, { editable: true })));
  trs.push(teacherNoteRow(widths));
  children.push(makeTable(trs, widths));
  children.push(P(""));
}

sentenceTable("Node 1 · Present tense sentences (SENTENCES_PRESENT_TEST)", [
  ["puella deam amat.", "The girl loves the goddess.", "is loving; likes"],
  ["pater filiam rogat.", "The father asks the daughter.", "questions; is asking"],
  ["femina in insula habitat.", "The woman lives on the island.", "is living"],
  ["dea pulchra ad terram navigat.", "The beautiful goddess sails towards the land.", "to the land; is sailing"],
  ["regina tristis clamat, nam deus appropinquat.", "The sad queen shouts, for the god approaches.", "is shouting; draws near"],
  ["puella laeta patri imperat, et pater festinat.", "The happy girl orders the father, and the father hurries.", "joyful; is ordering; rushes"],
  ["ego feminam oro, sed dea non clamat.", "I beg the woman, but the goddess does not shout.", "plead; is not shouting"],
  ["multi dei insulam oppugnant, et ibi feminae clamant.", "Many gods attack the island, and there the women shout.", "are attacking; are shouting"],
  ["deus ingens per urbem festinat, et regina puellas liberat.", "The huge god hurries through the city, and the queen frees the girls.", "enormous; rushes; sets free"],
  ["pater puellam necat, et dea tristis deos orat.", "The father kills the girl, and the sad goddess begs the gods.", "murders; pleads with; prays to"],
]);

sentenceTable("Node 1 · Present-system sentences (imperfect + future)", [
  ["dea clamabat.", "The goddess was shouting.", "used to shout; kept shouting; shouted"],
  ["pater navigabit.", "The father will sail.", "will be sailing; is going to sail"],
  ["puella tum clamabat, et pater navigabat.", "The girl was then shouting, and the father was sailing.", "then was shouting; used to shout"],
  ["regina feminam rogabit, et femina deam orabit.", "The queen will ask the woman, and the woman will beg the goddess.", "is going to ask; will beg; will pray"],
  ["multi dei subito urbem oppugnabant, sed regina in insula habitabat.", "Many gods were suddenly attacking the city, but the queen was living on the island.", "used to attack; was living"],
  ["puella pulchra in urbem festinabit, et pater clamabit.", "The beautiful girl will hurry into the city, and the father will shout.", "will rush; will shout"],
  ["dea me amabat, sed pater tum non orabat.", "The goddess was loving me, but the father was not then begging.", "loved me; was not begging then"],
  ["dea patrem liberabit, et pater deae tum imperabit.", "The goddess will free the father, and the father will then order the goddess.", "will set free; will then order"],
  ["regina illa deum laetum putabat, sed dea non orabat.", "That queen was thinking the god happy, but the goddess was not begging.", "thought; considered"],
  ["ingens navis per terram navigabat, et puella pulchra clamabat.", "A huge ship was sailing through the land, and the beautiful girl was shouting.", "enormous; used to sail; kept shouting"],
]);

sentenceTable("Node 1 · Perfect & Pluperfect sentences (SENTENCES_ACTIVE)", [
  ["puella clamavit.", "The girl shouted.", "has shouted; did shout"],
  ["pater feminam rogavit.", "The father asked the woman.", "has asked; questioned"],
  ["dea pulchra deum amavit, et deus clamavit.", "The beautiful goddess loved the god, and the god shouted.", "has loved; liked; has shouted"],
  ["regina filiam non liberaverat, sed pater domum festinavit.", "The queen had not freed the daughter, but the father hurried home.", "had not set free; hurried homeward"],
  ["multi dei ad insulam navigaverunt, et puellas necaverunt.", "Many gods sailed to the island, and killed the girls.", "sailed towards; have sailed; murdered"],
  ["pater ingens puellam amaverat, sed puella tristis deum oraverat.", "The huge father had loved the girl, but the sad girl had begged the god.", "enormous; had liked; had pleaded; had prayed"],
  ["illa dea ad tristem feminam appropinquavit, et clamabat.", "That goddess approached the sad woman, and was shouting.", "drew near"],
  ["regina urbem oppugnavit, et prope insulam habitavit.", "The queen attacked the city, and lived near the island.", "has attacked; dwelt close to"],
  ["ego deos rogaveram, sed etiam tum non clamaverant.", "I had asked the gods, but even then they had not shouted.", "still then; had not cried out"],
  ["pater mihi imperavit, et dea feminam pulchram putaverat.", "The father ordered me, and the goddess had thought the woman beautiful.", "has ordered; had considered"],
]);

sentenceTable("Node 1 · Perfect Passive Participle sentences (SENTENCES_PPP)", [
  ["puella liberata clamavit.", "The girl, having been freed, shouted.", "freed girl; once freed"],
  ["femina necata erat.", "The woman had been killed.", "had been murdered"],
  ["dea oppugnata ad insulam navigabat.", "The goddess, having been attacked, was sailing to the island.", "was sailing towards"],
  ["pater filiam amatam rogavit.", "The father asked the loved daughter.", "asked the beloved daughter; the having-been-loved daughter"],
  ["regina liberata puellam tristem amavit.", "The queen, having been freed, loved the sad girl.", "freed queen; once freed; had liked"],
  ["deus necatus erat, et dea clamabat.", "The god had been killed, and the goddess was shouting.", "had been murdered; kept shouting"],
  ["multae feminae oratae erant, sed reginae laetae non festinaverunt.", "Many women had been begged, but the happy queens did not hurry.", "pleaded with; prayed to; joyful; did not rush"],
  ["puella oppugnata patrem oravit, et pater feminas liberavit.", "The girl, having been attacked, begged the father, and the father freed the women.", "pleaded with; set free"],
  ["dea tristis deum necatum amaverat, sed deus imperatus erat.", "The sad goddess had loved the killed god, but the god had been ordered.", "slain; had been given orders"],
  ["ingens navis oppugnata ad terram navigabat, et multi dei clamaverunt.", "The huge ship, having been attacked, was sailing to the land, and many gods shouted.", "enormous; was sailing towards"],
]);

children.push(H("Node 1 · Review set (SENTENCES_REVIEW)", HeadingLevel.HEADING_3));
children.push(P("Mixed-tense exam-style sentences. Teacher gap noted in memory: add quod/postquam exemplars."));
children.push(PR([new TextRun({ text: "Teacher notes: ", bold: true, italics: true, color: "666666" })]));
children.push(P(""));

// Node 1 vocab
children.push(H("Node 1 · Vocabulary", HeadingLevel.HEADING_3));
const n1vocabRows = [
  headerRow(["Latin", "English", "Category", "Edits / also accept"], [1800, 3000, 1700, 2860]),
  ...[
    ["amo, amare, amavi, amatus", "I love, to love, I loved, loved", "verb"],
    ["clamo, clamare, clamavi, clamatus", "I shout, to shout, I shouted, shouted", "verb"],
    ["festino, festinare, festinavi", "I hurry, to hurry, I hurried", "verb"],
    ["habito, habitare, habitavi, habitatus", "I live, to live, I lived, lived in", "verb"],
    ["impero, imperare, imperavi, imperatus (+dat)", "I order (+ dative)", "verb"],
    ["libero, liberare, liberavi, liberatus", "I free, set free", "verb"],
    ["neco, necare, necavi, necatus", "I kill, murder", "verb"],
    ["navigo, navigare, navigavi", "I sail", "verb"],
    ["oppugno, oppugnare, oppugnavi, oppugnatus", "I attack", "verb"],
    ["oro, orare, oravi, oratus", "I beg, plead with, pray to", "verb"],
    ["puto, putare, putavi, putatus", "I think, consider (+ double acc.)", "verb"],
    ["rogo, rogare, rogavi, rogatus", "I ask, question", "verb"],
    ["appropinquo, appropinquare, appropinquavi", "I approach, draw near", "verb"],
    ["puella, -ae (f)", "girl", "noun"],
    ["dea, -ae (f)", "goddess", "noun"],
    ["femina, -ae (f)", "woman", "noun"],
    ["pater, patris (m)", "father", "noun"],
    ["filia, -ae (f)", "daughter", "noun"],
    ["insula, -ae (f)", "island", "noun"],
    ["regina, -ae (f)", "queen", "noun"],
    ["deus, -i (m)", "god", "noun"],
    ["terra, -ae (f)", "land, country", "noun"],
    ["urbs, urbis (f)", "city", "noun"],
    ["navis, navis (f)", "ship", "noun"],
    ["domum", "home, homewards", "noun (acc. of motion)"],
    ["pulcher, pulchra, pulchrum", "beautiful", "adj"],
    ["tristis, -e", "sad", "adj"],
    ["laetus, -a, -um", "happy, joyful", "adj"],
    ["ingens, ingentis", "huge, enormous", "adj"],
    ["multus, -a, -um", "much, many", "adj"],
    ["ego", "I", "pronoun"],
    ["me", "me (acc.)", "pronoun"],
    ["mihi", "to me, for me", "pronoun (dat.)"],
    ["ille, illa, illud", "that", "demonstrative"],
    ["in (+ acc)", "into, onto", "prep (+ACC)"],
    ["in (+ abl)", "in, on", "prep (+ABL)"],
    ["ad (+ acc)", "to, towards", "prep (+ACC)"],
    ["per (+ acc)", "through", "prep (+ACC)"],
    ["prope (+ acc)", "near", "prep (+ACC)"],
    ["et", "and", "conj"],
    ["sed", "but", "conj"],
    ["nam", "for", "conj"],
    ["-que", "and", "conj (enclitic)"],
    ["non", "not", "adv"],
    ["ibi", "there", "adv"],
    ["tum", "then", "adv"],
    ["subito", "suddenly", "adv"],
    ["etiam", "also, even", "adv"],
  ].map(r => dataRow([r[0], r[1], r[2], ""], [1800, 3000, 1700, 2860], { editable: true })),
  teacherNoteRow([1800, 3000, 1700, 2860]),
];
children.push(makeTable(n1vocabRows, [1800, 3000, 1700, 2860]));

// ---- NODE 2 ----
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Node 2 — 2nd Conjugation (Top 150)", HeadingLevel.HEADING_2));
children.push(P("Status: NOT YET REWRITTEN. The structure will mirror Node 1 (same 13–16 sets). Principal parts and vocab below are the target scope; sentences to be authored.", { run: { italics: true, color: "A04040" } }));

const n2verbs = [
  ["teneo, tenere, tenui, tentus", "I hold"],
  ["habeo, habere, habui, habitus", "I have"],
  ["appareo, apparere, apparui", "I appear"],
  ["iubeo, iubere, iussi, iussus", "I order"],
  ["persuadeo, persuadere, persuasi (+ dat)", "I persuade (+ dative)"],
  ["video, videre, vidi, visus", "I see"],
];
const widths2 = [3600, 3000, 2760];
const n2rows = [headerRow(["Latin principal parts", "English", "Edits / notes"], widths2)];
n2verbs.forEach(v => n2rows.push(dataRow([v[0], v[1], ""], widths2, { editable: true })));
n2rows.push(teacherNoteRow(widths2));
children.push(H("Node 2 · Verbs", HeadingLevel.HEADING_3));
children.push(makeTable(n2rows, widths2));

children.push(H("Node 2 · Additional vocabulary", HeadingLevel.HEADING_3));
const n2voc = [
  ["silva, -ae (f)", "wood, forest"],
  ["amicus, -i (m)", "friend"],
  ["gladius, -i (m)", "sword"],
  ["filius, -i (m)", "son"],
  ["omnis, -e", "every, all"],
  ["tu", "you (sg.)"],
  ["te", "you (acc. sg.)"],
  ["eum / eam", "him / her"],
  ["ei", "to him, to her (dat.)"],
  ["e / ex (+ abl)", "out of, from"],
  ["a / ab (+ abl)", "from, by"],
  ["igitur", "therefore"],
  ["tamen", "however"],
  ["statim", "immediately"],
  ["noli / nolite", "don't (prohibitive)"],
  ["vix", "scarcely, hardly"],
  ["mox", "soon"],
  ["iterum", "again"],
  ["enim", "for"],
];
const w2 = [2600, 3400, 3360];
const n2vr = [headerRow(["Latin", "English", "Edits / notes"], w2)];
n2voc.forEach(v => n2vr.push(dataRow([v[0], v[1], ""], w2, { editable: true })));
n2vr.push(teacherNoteRow(w2));
children.push(makeTable(n2vr, w2));

sentenceTable("Node 2 · Sentences — TO BE AUTHORED", [
  ["(teacher to supply)", "(teacher to supply)", ""],
  ["(teacher to supply)", "(teacher to supply)", ""],
  ["(teacher to supply)", "(teacher to supply)", ""],
]);

// ---- NODE 3 ----
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Node 3 — 3rd Conjugation", HeadingLevel.HEADING_2));
children.push(P("Status: NOT YET REWRITTEN.", { run: { italics: true, color: "A04040" } }));
const n3verbs = [
  ["dico, dicere, dixi, dictus", "I say"],
  ["duco, ducere, duxi, ductus", "I lead"],
  ["discedo, discedere, discessi", "I leave, depart"],
  ["peto, petere, petivi, petitus", "I seek, make for, ask for"],
  ["quaero, quaerere, quaesivi, quaesitus", "I search for"],
  ["cogo, cogere, coegi, coactus", "I force, compel"],
  ["relinquo, relinquere, reliqui, relictus", "I leave behind"],
  ["occido, occidere, occidi, occisus", "I kill"],
  ["cognosco, cognoscere, cognovi, cognitus", "I find out, get to know"],
  ["constituo, constituere, constitui, constitutus", "I decide"],
  ["pono, ponere, posui, positus", "I put, place"],
  ["facio, facere, feci, factus", "I make, do"],
  ["accipio, accipere, accepi, acceptus", "I receive, accept"],
  ["cupio, cupere, cupivi, cupitus", "I want, desire"],
  ["effugio, effugere, effugi", "I escape"],
  ["conspicio, conspicere, conspexi, conspectus", "I notice, catch sight of"],
];
const w3 = [3600, 3000, 2760];
const n3rows = [headerRow(["Latin principal parts", "English", "Edits / notes"], w3)];
n3verbs.forEach(v => n3rows.push(dataRow([v[0], v[1], ""], w3, { editable: true })));
n3rows.push(teacherNoteRow(w3));
children.push(H("Node 3 · Verbs", HeadingLevel.HEADING_3));
children.push(makeTable(n3rows, w3));

children.push(H("Node 3 · Additional vocabulary", HeadingLevel.HEADING_3));
const n3voc = [
  ["comes, comitis (m/f)", "companion"],
  ["manus, -us (f)", "hand; band (of men)"],
  ["caput, capitis (n)", "head"],
  ["mors, mortis (f)", "death"],
  ["iter, itineris (n)", "journey, route"],
  ["nihil", "nothing"],
  ["verbum, -i (n)", "word"],
  ["facilis, -e", "easy"],
  ["dirus, -a, -um", "dreadful"],
  ["solus, -a, -um", "alone"],
  ["alius, -a, -ud", "other, another"],
  ["eius", "his, her, its"],
  ["se", "himself / herself / themselves"],
  ["suus, -a, -um", "his own, her own, their own"],
  ["cum (+ abl)", "with"],
  ["iam", "now, already"],
  ["dum", "while"],
  ["simulac", "as soon as"],
  ["deinde", "then, next"],
  ["nunc", "now"],
  ["tandem", "at last, finally"],
  ["inquit", "he/she says, said"],
  ["consilium cepi", "I made a plan"],
  ["conatur", "he/she tries"],
];
const wv3 = [2600, 3400, 3360];
const n3vr = [headerRow(["Latin", "English", "Edits / notes"], wv3)];
n3voc.forEach(v => n3vr.push(dataRow([v[0], v[1], ""], wv3, { editable: true })));
n3vr.push(teacherNoteRow(wv3));
children.push(makeTable(n3vr, wv3));

sentenceTable("Node 3 · Sentences — TO BE AUTHORED", [["(teacher to supply)", "(teacher to supply)", ""]]);

// ---- NODE 4 ----
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Node 4 — 4th Conjugation", HeadingLevel.HEADING_2));
children.push(P("Status: NOT YET REWRITTEN. Teacher to confirm verb list and vocab.", { run: { italics: true, color: "A04040" } }));
const placeholder = [headerRow(["Latin", "English", "Notes"], [2800, 3200, 3360])];
["audio, audire, audivi, auditus — I hear / listen to",
 "venio, venire, veni, ventus — I come",
 "invenio, invenire, inveni, inventus — I find",
 "scio, scire, scivi, scitus — I know",
 "nescio, nescire, nescivi, nescitus — I do not know",
 "dormio, dormire, dormivi — I sleep"].forEach(v => {
  const [l,e] = v.split(" — ");
  placeholder.push(dataRow([l, e, ""], [2800, 3200, 3360], { editable: true }));
});
placeholder.push(teacherNoteRow([2800, 3200, 3360]));
children.push(H("Node 4 · Likely verb list (confirm)", HeadingLevel.HEADING_3));
children.push(makeTable(placeholder, [2800, 3200, 3360]));
sentenceTable("Node 4 · Sentences — TO BE AUTHORED", [["(teacher to supply)", "(teacher to supply)", ""]]);

// ---- NODE 5 ----
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Node 5 — Irregular: esse + possum", HeadingLevel.HEADING_2));
children.push(P("Status: NOT YET REWRITTEN.", { run: { italics: true, color: "A04040" } }));
const n5 = [headerRow(["Latin", "English", "Notes"], [2800, 3200, 3360]),
  dataRow(["sum, esse, fui", "I am, to be, I was / have been", ""], [2800, 3200, 3360], { editable: true }),
  dataRow(["possum, posse, potui", "I am able, can", ""], [2800, 3200, 3360], { editable: true }),
  teacherNoteRow([2800, 3200, 3360]),
];
children.push(makeTable(n5, [2800, 3200, 3360]));
sentenceTable("Node 5 · Sentences — TO BE AUTHORED", [["(teacher to supply)", "(teacher to supply)", ""]]);

// ---- NODE 6 ----
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Node 6 — Irregular: eo + compounds", HeadingLevel.HEADING_2));
children.push(P("Status: NOT YET REWRITTEN.", { run: { italics: true, color: "A04040" } }));
const n6 = [headerRow(["Latin", "English", "Notes"], [2800, 3200, 3360]),
  ...[
    ["eo, ire, ivi / ii", "I go"],
    ["exeo, exire, exivi / exii", "I go out"],
    ["redeo, redire, redivi / redii", "I return, go back"],
    ["adeo, adire, adivi / adii", "I approach"],
    ["pereo, perire, perivi / perii", "I perish, die"],
    ["transeo, transire, transivi / transii", "I cross"],
  ].map(v => dataRow([v[0], v[1], ""], [2800, 3200, 3360], { editable: true })),
  teacherNoteRow([2800, 3200, 3360]),
];
children.push(makeTable(n6, [2800, 3200, 3360]));
sentenceTable("Node 6 · Sentences — TO BE AUTHORED", [["(teacher to supply)", "(teacher to supply)", ""]]);

// ---------- VALID TRANSLATIONS & MARKING ----------
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(H("Valid translations & marking behaviour", HeadingLevel.HEADING_1));
children.push(P("The marker (y11/marking.py) automatically accepts these equivalences. Strike any you want tightened, or add rows to loosen."));

const mRows = [
  headerRow(["Rule", "Example accepted", "Keep / remove"], [4000, 3200, 2160]),
  dataRow(["Simple past ⇄ progressive past", "\"loved\" ⇄ \"was loving\" (imperfect)", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Perfect has 3 renderings", "\"has shouted\" / \"shouted\" / \"did shout\"", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Parenthetical optional gloss", "\"(to) home\" → accepts \"home\" OR \"to home\"", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Slash alternatives, order-agnostic", "mihi → \"to me\", \"for me\", \"to me, for me\", \"to me / for me\"", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Typo tolerance (Levenshtein 1)", "\"godess\" → accepted with advisory, not rejected", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Punctuation differences", "trailing period, comma, apostrophe — silently accepted", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Tense mismatch", "REJECTED with hint (no silent accept)", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Number mismatch (sg/pl)", "REJECTED with sg/pl near-miss hint", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Person mismatch", "REJECTED with person near-miss hint", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["in +ABL vs in +ACC (in/into)", "REJECTED with case-based hint", ""], [4000, 3200, 2160], { editable: true }),
  dataRow(["Partial vocab meanings", "REJECTED with \"list all its meanings\" hint", ""], [4000, 3200, 2160], { editable: true }),
  teacherNoteRow([4000, 3200, 2160]),
];
children.push(makeTable(mRows, [4000, 3200, 2160]));

// ---------- OPEN QUESTIONS ----------
children.push(H("Known gaps / open questions for the teacher", HeadingLevel.HEADING_1));
children.push(bullet("SENTENCES_REVIEW: add quod/postquam exemplars (per memory note)."));
children.push(bullet("Preposition case badges: confirm the final list for +ACC/+ABL/+DAT tags in vocab (ad, prope, per, trans, post, ante, apud, circum, contra, inter, propter, sub, super, sine, cum, de, ex/e, a/ab, pro)."));
children.push(bullet("Nodes 2–6 sentences: to be authored to match Node 1 pattern."));
children.push(bullet("Principal-parts screens: confirm teacher wants -re green and -tus yellow visible in the infinitive and PPP pattern rows."));
children.push(bullet("Pupil completion data: confirm you want the database reset (completed_sets / sessions wiped, roster preserved)."));
children.push(PR([new TextRun({ text: "Teacher notes: ", bold: true, italics: true, color: "666666" })]));

// ---------- SIGN-OFF ----------
children.push(H("Sign-off", HeadingLevel.HEADING_1));
children.push(P("Teacher name: ______________________________     Date: ______________"));
children.push(P("Approval to proceed with the edits marked above: ☐"));

// ---------- DOC ----------
const doc = new Document({
  creator: "Claude",
  title: "Latin GCSE Mastery Platform — Curriculum & Design Overview",
  styles: {
    default: { document: { run: { font: "Calibri", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Calibri", color: "1F3A5F" },
        paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Calibri", color: "2E5E8A" },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Calibri", color: "4A4A4A" },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Latin GCSE Mastery Platform — Curriculum & Design Overview", size: 18, color: "888888" })],
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

Packer.toBuffer(doc).then(buf => {
  const out = "C:\\Users\\mmhun\\Desktop\\y11_latin_gcse\\CURRICULUM_OVERVIEW.docx";
  fs.writeFileSync(out, buf);
  console.log("Wrote", out, "(" + buf.length + " bytes)");
});
