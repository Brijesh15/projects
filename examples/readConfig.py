#!/usr/bin/python
"""
/* File Name readConfig.py
 * Copyright (C) HAE Innovations - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 *
 *	http://haeinnovations.com/
 *
 * This file is part of simplifyINV.
 *
 * simplifyINV can not be copied and/or distributed without the express
 * permission of HAE Innovations,
 * Written by Ranjeet Singh (ranjeet.singh@haeinnovations.com), January 2016
 */
"""

import xml.etree.cElementTree as ET
import copy
from ConfigParser import SafeConfigParser

class Config(object):
    def __init__(self, file_path):
        self.file = file_path
        self.config_dict = {}
        if '.xml' in file_path:
            self.read_file_XML(file_path)
            return
        elif '.txt' in file_path:
            self.read_file_TXT(file_path)
        else:
            print('File Format not supported')
    #     self.metaConfigPath = metaConfigPath

    def read_file_XML(self, file):
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()

    def create_dict_xml(self):

        for node in self.root:
            temp = {}
            for value in node:
                temp[value.tag.upper()] = value.text
            if temp == {}:
                self.config_dict[node.tag.upper()] = node.text
            else:
                self.config_dict[node.attrib.values()[0].upper()] = copy.deepcopy(temp)
            temp.clear()
        print self.config_dict

    def read_file_TXT(self,file):

        self.config = SafeConfigParser()
        self.config.read(file)

    def create_dict_txt(self):
        # configDict = {}
        for section in self.config.sections():
            temp = {}
            for key,value in self.config.items(section):
                temp[key] = value
            self.configDict[section] = copy.deepcopy(temp)
        print self.configDict
        # return self.configDict

    def update_element(self, node, new_value, attribute = None, tag = None  ):#,node, attribute, value):
        print('Update file')
        result = self.search_node(node, attribute, tag)
        result.text = new_value
        if attribute:
            self.config_dict[attribute][tag] = new_value
        else:
            self.config_dict[node] = new_value
        self.tree.write(self.file)
        print self.config_dict

    def search_node(self, node, attribute=None, tag=None):
        for temp_node in self.root.iter(node):
            if not attribute:
                return temp_node
            if temp_node.attrib.values()[0] == attribute:
                return temp_node.find(tag)

    def update_attribute(self):
        pass

    def get_config_dict(self, node_name=None):
        if node_name:
            return self.config_dict[node_name]
        return self.config_dict


if __name__ == '__main__':
    r = Config('/home/wavenet/vaibhav/source/testAutomationTool/configuration/meta_config.xml')
    # r.readFileTxt('../configuration/ueConfig.xml')
    # r.readFileXML('../configuration/interface_config.xml')
    r.create_dict_xml()
    d = r.get_config_dict()
    print d['CFGIDINUSE']
    # if not d['roamMcc'.upper()]:
    #     print 'yes'
    # else:
    #     print 'no'
    # print d['roamMcc'.upper()]

    # r.update_element('cfgId','sprint','2','name')
    # print r.config_dict

    # from xml.etree import cElementTree as etree
    # xml = """
    # <TrdCaptRpt RptID="10000001" TransTyp="0">
    #     <RptSide Side="1" Txt1="XXXXX">wavenet<Pty ID="XXXXX" R="1"/>
    #     </RptSide>
    # </TrdCaptRpt>
    # """
    #
    # root = etree.fromstring(xml)
    # # root = etree.parse('test.xml')
    #
    # rpt_side = root.find('RptSide')
    # print rpt_side.get('Side')
    # rpt_side.set('Txt1', 'Updated')
    # # lst=root.getroot
    # # print lst
    # for child in root:
    #     print child.tag, child.attrib
    # print 'aaa',rpt_side.text
    # rpt_side.text='wavenetsol'
    # print 'aaa',rpt_side.text
    # pty = rpt_side.find('Pty')
    # # print pty.
    #
    # pty.set('ID', 'Updated')
    # pty.set('ID2','shooshohso')
    # pty.set('ID2','uuueueuue')
    # print etree.tostring(root)
    # # print etree.tostring(root.getroot())