import sys
import math
def armstrong(num):
    l = len(str(num))
    s = 0
    temp = num
    while (temp!=0):
        r = temp%10
        s = s + pow(r,l)
        temp = temp//10
    print(num == s)

armstrong(4)

def ntharmstrong(n):
    #i = n
    count = 0
    for num in range(1,sys.maxsize):
        #print(num)
        l = len(str(num))
        s = 0
        temp = num
        while (temp):
            r = temp%10
            s = s + pow(r,l)
            temp = temp//10
        if num == s:
            count+=1
        if n == count:
            return num

print(ntharmstrong(12))

def armstrong1(num):
    l = len(str(num))
    s = 0
    for i in str(num):
        s+=pow(int(i),l)
    print(s)
    return s == num


print(armstrong1(34))
