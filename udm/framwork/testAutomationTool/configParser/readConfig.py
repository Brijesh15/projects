import copy
import xml.etree.ElementTree as ET
import configparser
import yaml
#from xml_operation import xmlOperation
#import os
#path = os.path.dirname(os.path.abspath(__file__))

class Config(object):

    def __init__(self, file_path):

        #self.x = xmlOperation()
        self.file = file_path
        self.config_dict = {}
        if file_path.endswith(".xml"):
            self.read_file_XML(file_path)
            return
        elif file_path.endswith(".cfg"):
            self.read_file_CFG(file_path)
            return
        elif file_path.endswith(".yaml"):
            self.read_file_YAML(file_path)
            return
        else:
            print('File Format not supported')

    def read_file_XML(self, file):
        """
        parse the given xml file
        """
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()

    def read_file_CFG(self, file):
        """
        parse the given cgf file
        """
        self.config = configparser.ConfigParser()
        self.config.read(file)

    def read_file_YAML(self, file):
        """
        parse the given cgf file
        """
        with open(file, 'r') as file:
            self.data = yaml.safe_load(file)

    def create_dict_xml(self):
        """
        create a dictionary of all nodes in the xml
        """
        for node in self.root:
             temp = {}
             for value in node:
                 temp[value.tag.upper()] = value.text
             if not temp:
                 self.config_dict[node.tag.upper()] = node.text
             else:
                 self.config_dict[list(node.attrib.values())[0].upper()] = copy.deepcopy(temp)
             temp.clear()
        print(self.config_dict)

    def update_xml_element(self, nodeName, tagsValues):
        """
        update and set the given node
        args:
            nodeName: name of the node
            optionsValues: list of dictionary where keys are tags and values are text of tags
        """
        for tagValue in tagsValues:
            tag = list(tagValue.keys())[0]
            value = list(tagValue.values())[0]
            element= "./*[@name='{0}']/{1}".format(nodeName,tag)
            if self.tree.findall(element)[0].text == value:
                continue
            self.tree.findall(element)[0].text = value
        self.tree.write(self.file, method='html')

    def get_tag_value(self, nodeName, tagList):
        """
        return dictionary, where tag is key and tag's value is value of the given node and tag
        """
        Dict = {}
        for element in self.root.findall("./node"):
            if element.attrib.get("name") == nodeName:
                for tagName in tagList:
                    Dict[tagName] = self.root.find(".//*[@name='" + nodeName + "']/%s"%(tagName)).text
                print(Dict)
                return Dict
        return False

    def create_dict_cfg(self):
        """
        create a dictionary of all nodes in the cfg
        """
        for section in self.config.sections():
             temp = {}
             #print(self.config[section])
             for key in self.config[section]:
                 #print(self.config[section][key])
                 temp[key] = self.config[section][key]
             self.config_dict[section.upper()] = copy.deepcopy(temp)
             temp.clear()
        print(self.config_dict)

    def get_section_value(self, section, keyList):
        """
        return dictionary, where section key is key and sections's value is value of the given section and key
        """
        Dict = {}
        for key in keyList:
            Dict[key] = self.config[section][key]
        print(Dict)
        return Dict

    def create_config_parser(self, section, optionsValues):
        """
        update and set the given section
        args:
            section: section name
            optionsValues: list of dictionary where keys are options and values are values of option
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        for optionValue in optionsValues:

            option = list(optionValue.keys())[0]
            value = list(optionValue.values())[0]
            if not self.config.has_option(section, option):
                self.config.set(section, option, value)
            elif self.config.get(section, option) == value:
                print("Already set")
            else:
                self.config.set(section, option, value)
        with  open('config1.cfg', 'w') as configfile:
            self.config.write(configfile)

    def remove_section(self, section):
        """
        remove the given section
        """
        if self.config.has_section(section):
            self.config.remove_section(section)
            return True
        return "section not found in the configuration file"

    def remove_option(self, section, option):
        """
        remove the given option from given section
        """
        if self.config.has_option(section, option):
            self.config.remove_option(section, option)
            return True
        return "option not found in the configuration file"

    def get_config_dict(self, node_name=None):
        """
        return the value of given key from dictionary
        return hole dictionary if key not provided
        """
        if node_name:
            return self.config_dict[node_name]
        return self.config_dict

    #def xml(self):

    #   top = self.x.xml_top('jdhffhh',attr={'name':'brijesh'})
    #   self.x.xml_child(top,"h",'H')
    #   self.x.xml_child(top,"i", 'I')
    #   self.x.xml_child(top,"j")
    #   xml_write = self.x.xml_print(top)
    #   xml_write = "\n".join([i for i in xml_write.split("\n") if i.strip()])
    #   self.x.xml_write(xml_write, 'abc.xml')

    def get_node_data(self, key):

        """Pull all values of specified key from nested Dict."""

        arr = []
        obj = self.data.copy()
        def extract(obj, arr, key):
            """Recursively search for values of key in dict tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == key:
                        arr.append(v)
                    elif isinstance(v, (dict, list)):
                        extract(v, arr, key)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr[0]
        results = extract(obj, arr, key)
        return results

    def get_all_data(self):

        output = {}
        for k in self.data.keys():
            output[k] = self.data[k]
        return output

if __name__ == "__main__":
    #pass
    c= Config("interfaceConfig.yaml")
    print(c.get_node_data('systemConfigurationin'))
    #c.get_section_value('bitbucket.org', ['Compression', 'CompressionLevel'])
    #c.get_get_tag_value('pgw', ['ip', 'port'])
    #c.create_config_parser('default', [{'unjjnska naam':'chaudharyhjbdhb'}, {'name':'wavenet'}])
    #c.update_xml_element('host', [{'passwd': 'ROOT123'}, {'user_name': 'ROOT'}])
    #c.xml()

