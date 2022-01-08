from xml.etree.ElementTree import Element, SubElement, Comment, tostring, parse, ElementTree
from xml.sax.saxutils import escape
from xml.dom import minidom
#import xmltodict


class xmlOperation():

    def xml_print(self, top):
        """
        return pretty string format of xml
        """
        rough_string = tostring(top)
        reparse = minidom.parseString(rough_string)
        return reparse.toprettyxml(indent=" ").replace('&quot;', '"')

    def xml_top(self, top, attr={}):
        """
        Create a element instance and return it
        """
        top = Element(top, attr)
        return top

    def xml_child(self, top, child, child_text=None, attr={}):
        """
        add subelement to element tag and return it
        """
        child = SubElement(top, child, attr)
        child.text = child_text
        return child

    def xml_find(self, root, tag=''):
        try:
            tag_list = root.findall(".//" + tag)
            return tag_list
        except:
            return []

    def xml_write(self, top, file_name):
        """
        write xml tree in a file
        """
        with open(file_name, 'w+') as f:
            f.write(top)

#    def covert_jsontoxml(args, file_name, root=''):
#        """
#        This Function converts json to xml
#        :param args:
#        :return:
#        """
#        try:
#            # if type(args) == dict:
#            if root: args = {root: args}
#            xmlString = xmltodict.unparse(args, pretty=True, full_document=False)
#            # if type(args) == str:
#            #   xmlString = xmltodict.unparse(json.loads(args), pretty=True, full_document=False)
#            # xml_file = (file_name + '_config.xml')
#            with open(file_name, 'w') as f:
#                f.write(xmlString)
#            return True
#        except Exception, e:
#            return "Error occurred while converting json to xml"
