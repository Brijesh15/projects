from xml.etree.ElementTree import Element , SubElement,Comment
from xml.etree import ElementTree
from xml.dom import minidom
import socket

s= socket.socket()
host = socket.gethostname()
port=12345
s.bind((host,port))
s.listen(3)
s1,addr=s.accept()
print "Thanks for connecting to client"

def create_xml_file(top):
        rough_string = ElementTree.tostring(top,'utf_8')

        reparsed = minidom.parseString(rough_string)
#        fo=open("c.xml","w+")
        s1.send(reparsed.toprettyxml(indent =""))
#	s1.send('hello python')
        s1.close()

#def prettiffy():
#       fo=open("c.xml","r+")
#        print fo.read(500)
#        fo.close()

top = Element('top')
comment=Comment('Generated for Python')
top.append(comment)
child = SubElement(top,'child')
child.text = 'this is child text.'
child_with_tail = SubElement(top,'child_with_tail')
child_with_tail.text = 'This child has regular text'
child_with_tail.tail = 'And "tail" text.'
child_with_entry_ref= SubElement(top,'child_with_entry_ref')
child_with_entry_ref.text='this & That'

create_xml_file(top)
#prettiffy()

