import json
import dicttoxml
import xmltodict
#args = json.dumps(args)
#args = json.loads(args)
#print("*WARN*",args)
#args_xml = dicttoxml.dicttoxml(args)
jsonString = '{"id": 1,"name": "Foo","price": 123,"tags": ["Bar","Eek"],"stock": {"warehouse": 300,"retail": 20}}'
print(type(jsonString))
#jsonString = '{0}'.format(jsonString)
#with open('sample.json', 'w') as f:
#    f.write(jsonString)
 
#with open('sample.json', 'r') as f:
#    jsonString = f.read()
#print(jsonString) 
print('JSON input (sample.json):')
xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True,full_document=False)
#xmlString = xmltodict.unparse(jsonString, pretty=True,full_document=False)
 
print('\nXML output(output.xml):')
print(xmlString)
 
with open('output.xml', 'w') as f:
    f.write(xmlString)
