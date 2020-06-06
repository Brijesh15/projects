import xml.etree.ElementTree as ET

#core_network_type = 'CND'
#core_network = ET.Element('core_network')
#core_nw_type = ET.SubElement(core_network,'core_nw_type')
#print(core_nw_type.tag)
#core_nw_type.text = core_network_type
#mycore_nw_type = ET.tostring(core_network)
#myfile = open("core_network_type.xml", "w")
#myfile.write(mycore_nw_type)

tree = ET.parse("items2.xml")
root = tree.getroot()
print root	
for subelem in root:
	
