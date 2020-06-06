import xml.etree.ElementTree as ET
config_file = '/home/brijesh/hae/Framework/source/testAutomationTool/configuration/enodeb_config.xml'
cfg_id ='1'	
tree = ET.parse(config_file)
root = tree.getroot()
tag = 'ip'
#ss = root.find(".//*[@config='" + "84711862-17C2-46AE-A4B3-AAB4070B3703" + "']/ip").text
#print(ss)
for element in root.findall("./node"):
    #print "name:",element.attrib.get("config")
    if element.attrib.get("config") == cfg_id:
        #root.find(".//node[@config='" + "%s"%(cfg_id) + "']/ip").text = '127.0.0.1'
        #tree.write(config_file)
        ip = root.find(".//node[@config='" + "%s"%(cfg_id) + "']/%s"%(tag)).text
        print ip
        #print ip
        #for item in root.iter('config'):
        #    print item.text
        
