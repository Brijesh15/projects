class UserMainCode(object):
    @classmethod
    def pairs(cls, input1):
        cnt = 0
        for i in range(0, input1):
            for j in range(0, input1):
                print(i,j)
                if gcd(i,j) == 1:
                    print("dhfhe")
                    cnt+=1
        return cnt

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b, a % b)


def hcf(x,y):
    while(y):
        x, y = y, x % y
    return x
obj=UserMainCode()
print(obj.pairs(4))
print(hcf(1,3))
