"""Parse CURRICULUM_SENTENCES.docx into structured JSON.

Doc structure per sentence block:
  Node X — <label>
  Focus: ...
  Set N — <tense label>
  # | Latin sentence | Ideal translation (GCSE vocab) | Accepted alternatives (marking points) | Teacher notes
  Then records: number, latin, ideal, <alt lines>, <teacher note lines>
Separator between records = line starting with digit + blank.
"""
import zipfile, re, json, sys

SRC = r'C:/Users/mmhun/Desktop/y11_latin_gcse/CURRICULUM_SENTENCES.docx'
z = zipfile.ZipFile(SRC)
xml = z.read('word/document.xml').decode('utf-8')

# Preserve paragraph breaks
xml = re.sub(r'</w:p>', '\n', xml)
xml = re.sub(r'<w:br[^/]*/>', '\n', xml)
# drop all other tags
text = re.sub(r'<[^>]+>', '', xml)
# unescape
text = text.replace('&amp;', '&').replace('&#x2019;', "'").replace('&#x201C;', '"').replace('&#x201D;', '"').replace('&#x2014;', '—').replace('&#x2013;', '–').replace('&quot;','"').replace('&lt;','<').replace('&gt;','>')
text = re.sub(r'[ \t]+\n', '\n', text)
lines = [l.strip() for l in text.split('\n')]

# Find node/set anchors
out = {}
current_node = None
current_set = None
i = 0
# Skip until the Node 1 section starts — we know it's around line 983
while i < len(lines) and not re.match(r'Node 1 — 1st Conjugation', lines[i]):
    i += 1

def is_num(s):
    return bool(re.match(r'^\d+$', s))

while i < len(lines):
    line = lines[i]
    m_node = re.match(r'^Node ([1-6])\s*[—–-]\s*(.+)$', line)
    if m_node:
        current_node = int(m_node.group(1))
        current_set = None
        out.setdefault(current_node, {'label': m_node.group(2), 'sets': {}})
        i += 1
        continue
    m_set = re.match(r'^Set (\d+)\s*[—–-]\s*(.+)$', line)
    if m_set and current_node:
        current_set = int(m_set.group(1))
        out[current_node]['sets'].setdefault(current_set, {'label': m_set.group(2), 'sentences': []})
        i += 1
        continue
    # §A, §B etc. for Nodes 5 / 6
    m_para = re.match(r'^§([A-Z])\s*[—–-]\s*(.+)$', line)
    if m_para and current_node:
        # map A->101, B->102 etc to avoid clashing with Set numbers
        letter = m_para.group(1)
        current_set = 100 + (ord(letter) - ord('A'))
        out[current_node]['sets'].setdefault(current_set, {'label': f'§{letter} — {m_para.group(2)}', 'sentences': []})
        i += 1
        continue
    # guard
    if current_node and current_set and current_set not in out[current_node]['sets']:
        current_set = None
    # sentence record: standalone integer line
    if current_node and current_set and is_num(line):
        num = int(line)
        # Skip blanks, gather non-blank lines until next integer or next Node/Set header
        j = i + 1
        buf = []
        while j < len(lines):
            nxt = lines[j]
            if not nxt:
                j += 1
                continue
            if is_num(nxt) and int(nxt) == num + 1:
                break
            if re.match(r'^Set \d+\s*[—–-]', nxt) or re.match(r'^Node [1-6]\s*[—–-]', nxt) or re.match(r'^§[A-Z]', nxt):
                break
            if is_num(nxt) and int(nxt) == 1 and buf:
                break
            if nxt == '#' or nxt.startswith('Latin sentence') or nxt.startswith('Ideal translation') or nxt.startswith('Accepted alternatives') or nxt == 'Teacher notes':
                j += 1
                continue
            buf.append(nxt)
            j += 1
        # First nonblank = latin. Second = ideal. Rest = alternatives (may include teacher notes in ALL-CAPS)
        if len(buf) >= 2:
            latin = buf[0]
            ideal = buf[1]
            rest = buf[2:]
            # Split rest into alternatives vs teacher notes (teacher notes tend to be ALL CAPS)
            alts = []
            teacher_notes = []
            for r in rest:
                # Heuristic: line mostly uppercase and longer than 10 chars = teacher note
                letters = [c for c in r if c.isalpha()]
                if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.6 and len(r) > 8:
                    teacher_notes.append(r)
                else:
                    alts.append(r)
            out[current_node]['sets'][current_set]['sentences'].append({
                'num': num,
                'latin': latin,
                'ideal': ideal,
                'alternatives': alts,
                'teacher_notes': teacher_notes
            })
        i = j
        continue
    i += 1

# Summarise
total = 0
for n in sorted(out):
    print(f'Node {n}: {out[n]["label"]}')
    for s in sorted(out[n]['sets']):
        cnt = len(out[n]['sets'][s]['sentences'])
        total += cnt
        print(f'  Set {s} ({out[n]["sets"][s]["label"]}): {cnt}')
print(f'TOTAL: {total}')

json.dump(out, open(r'C:/Users/mmhun/Desktop/y11_latin_gcse/_sentences_parsed.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
