import xml.etree.ElementTree as ET
import json
import codecs

def extract_vocab(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # xml namespaces
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    vocab_pairs = []
    
    # find all tables
    for tbl in root.findall('.//w:tbl', ns):
        # find all rows
        for tr in tbl.findall('.//w:tr', ns):
            cells = tr.findall('.//w:tc', ns)
            if len(cells) >= 2:
                # text from first cell
                lat = "".join(t.text for t in cells[0].findall('.//w:t', ns) if t.text)
                # text from second cell
                eng = "".join(t.text for t in cells[1].findall('.//w:t', ns) if t.text)
                lat = lat.strip()
                eng = eng.strip()
                if lat and eng:
                    vocab_pairs.append((lat, eng))
                    
    return vocab_pairs

if __name__ == '__main__':
    data = extract_vocab("doc1_unpacked/word/document.xml")
    with codecs.open("extracted_vocab.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Extracted {len(data)} items to extracted_vocab.json")
