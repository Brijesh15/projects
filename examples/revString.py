def rev(Str):

    n = len(Str)
    Str = list(Str)
    start = 0
    end = n - 1
    while start < end:

        if not Str[start].isalpha():
            start+=1
            continue
        elif not Str[end].isalpha():
            end-=1
            continue
        else:
            Str[start], Str[end] = (Str[end], Str[start])
            start+=1
            end-=1
            
    return "".join(Str)

s = "ab#hn$sl"
#s = "fd#k!&bj%%*"
print(s)
print(rev(s))
