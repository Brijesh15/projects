#Input:
str1 = "a2-4, b4-4, c6-9, d7-11, e18-21"
print("input: ")
print(str1)

#Output: (without duplicate numbers)
#list1 = [2, 3, 4, 6, 7, 8, 9, 10, 11, 18, 19, 20, 21]
lst2 = []
lst1 = str1.split(", ")
for i in lst1:
    i1 = i[1:].split("-")
    for j in range(int(i1[0]),int(i1[1]) +1 ):
        if j not in lst2:
            lst2.append(j)

print("output: ")
print(lst2)

