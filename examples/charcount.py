def countchar(s):
    s1 = ""
    for i in sorted(s):
        if i in s1:
            continue
        s1 = s1 + i + str(s.count(i))
    return s1

s = "bbrijesh"
print(countchar(s))

def varname(s):
    s = s.split("_")
    s2=""
    c = 0
    for i in s:
        if c == 0:
            s2= s2 + i
            c=1
            continue
        s2 = s2 + i[0].upper() + i[1:]
    print(s2)
    for j in s2:
        if j == j.upper():
            s2 = s2.replace(j, "_"+j.lower())
    print(s2)

s = "var_name_count_abc_cdw"
varname(s)

