from collections import Counter
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

xml_data = root.findall("channel/item/description")

words = []

for value in xml_data:
    description = value.text.lower().split()
    for index in range(len(description)):
        if len(description[index]) > 6:
            words.append(description[index])
            words.sort()
            c = Counter(words)
print(c.most_common(10))
