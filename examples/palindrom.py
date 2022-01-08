def palindrom(s):
    n = len(s)
    s1 = ""
    #for i in range(1,n+1):
        #print(-i)
        #print(s[-i])
    #    s1+=s[-i]

    start = 0
    end = n-1
    l = list(s)
    while start < end:
        l[start], l[end] = l[end], l[start]
        start+=1
        end-=1
  
    s1 = "".join(l)
    #print(s1)
    if s == s1:
        print("palindrom")
    else:
        print("not palindrom")

palindrom("brijesh")
