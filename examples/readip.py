ip = '192.168.126.120'
i = 0
IPaddr = ''
IP = ''
for a in range(0, 20):
#    print "a",a
    if  ip[a] == '.':
        if int(IP) < 10:
            IPaddr = IPaddr + '0' + hex(int(IP)).replace('0x','')
        else:
            IPaddr = IPaddr+hex(int(IP)).replace('0x','')
     #   a = a+1
        IP = ''
        continue
    IP = IP+ip[a] 
    if len(ip)-1 == a:
        if int(IP) < 10:
            IPaddr = IPaddr + '0' + hex(int(IP)).replace('0x','')
        else:
            IPaddr = IPaddr+hex(int(IP)).replace('0x','')
        break
    #a= a+1
print"IPaddr",IPaddr
