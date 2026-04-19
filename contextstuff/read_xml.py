import xml.etree.ElementTree as ET
import sys

def extract_text(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    # XML tags in docx have namespaces, we can just iter over everything and grab text
    texts = [elem.text for elem in root.iter() if elem.text and elem.text.strip()]
    return " ".join(texts)

print(extract_text(sys.argv[1]))
