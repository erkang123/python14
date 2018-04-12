import xml.etree.ElementTree as ET
tree = ET.parse('xmltest')
root = tree.getroot()
print(root)
print(root.tag)
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)
for node in root.iter('year'):
    print(node.text)