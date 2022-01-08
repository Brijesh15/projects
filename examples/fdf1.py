#Script Inputs:
Number = 9
Count = 4
Line = 3

#    Output:
#        9 8 7 6
#        8 7 6
#        7 6

for i in range(Line):
    for j in range(Number , Number - Count, -1):
        print("{0} ".format(j), end="")
    print("")    
    Number -=1
    Count -=1

