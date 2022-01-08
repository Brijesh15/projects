def sublist(A, sum):
    dict = {}
    dict.setdefault(0, []).append(-1)
    print(dict)
    sum1 = 0
    for i in range(len(A)):
        sum1 += A[i]
        if sum1 - sum in dict:
            print(*[A[value + 1: i +1] for value in dict.get(sum1 -sum)])
        dict.setdefault(sum1 , []).append(i)
        print(dict)

A = [3,4,-7,1,3,3,1,-4]
sum = 7
sublist(A, sum)
print("\n")
