import xml.etree.ElementTree as ET
def modifyetter(var):
    """
    """
    #sys_config = path + "/configuration/interface_config.xml"
    sys_config = "/home/brijesh/hae/Framework/source/testAutomationTool/configuration/interface_config.xml"
    try:
        tree = ET.parse(sys_config)
        root = tree.getroot()
        for element in root.findall("./node"):
            if element.attrib.get("name") == var:
                #ip = root.find(".//*[@name='" + var +"']/ip").text
                ip = root.find(".//*[@name='" + var +"']/ip").text = '8.8.8.8'
                print "ip",ip
                #return True
                #if fw_id:
                #    return fw_id
                tree.write(sys_config)
        return False
    except:
        print "error occurred while changing in xml", traceback.fromat_exc()
        return False


modifyetter('remoteFrame')
