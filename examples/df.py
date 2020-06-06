import sys
#print "argv:",sys.argv[1]
#kdh = 'i'
#print kdh
l = [('a','b'), ('c','d','e'),('f')]
outstr = 'a->b?c->d?e'
s=''
for t in l:
    s+='->'.join(t)
    s+='?'
s=s[0:-1]
print(s)
