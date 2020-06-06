import xml.etree.ElementTree as ET
tree = ET.parse('core_network_type.xml')  
root = tree.getroot()
print(root)
for elem in root:  
    print(elem)
    print(elem.text)
