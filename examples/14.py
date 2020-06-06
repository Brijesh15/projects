SIP_INSTANCE = 'id="urn:gsma:imei:99000488-941940-0"'
new = SIP_INSTANCE.replace('"',"")
print new
new = SIP_INSTANCE[1:-1].replace('id=','')
print new

