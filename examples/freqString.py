s="brijesh chaudhary"
lst=sorted(s)
set1=set(lst)
#print sorted(list(set1))
outstr=""
for char in sorted(list(set1)):
    if char == " ":
        continue
    outstr+=outstr.join(char)
    outstr+=outstr.join(str(s.count(char)))

print outstr
