l=[2,3,1,10]
subArray=0
for i in range(len(l)):
    subsum=0
    for j in range(i,len(l)):
        if (subsum+l[j]) <= 10:
            subsum+=l[j]
            subArray+=1
        else:
            break
print(subArray)
