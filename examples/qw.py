PLMN_ID = '{"311480", "0", "0", "0", "0", "0"}'
#print PLMN_ID.rstrip('0')
PLMN_ID=PLMN_ID.split(' ',1 )
#PLMN_ID=PLMN_ID.replace(",", '' )
#PLMN_ID=PLMN_ID.replace("{")
PLMN_ID = PLMN_ID[0]
PLMN_ID=PLMN_ID.replace("{", '')
PLMN_ID=PLMN_ID.replace(",", '')
print "plmn -id", PLMN_ID

