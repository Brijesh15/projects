from readConfig import Config
import xml.etree.ElementTree as ET
filepath = 'enodeb_config.xml'
meta_config = 'meta_config.xml'
#cfg_id = '77B0355D-EFAD-4124-8C91-C8324D77090C'
metatree = ET.parse(meta_config)
metaroot = metatree.getroot()
child = metaroot.find('cfgIdInUse')
print "clild",child.text
config = Config(filepath)
config.create_dict_xml()
print"hjhcbjhcc", config.get_config_dict(child.text)
