def c(array):
    def a():
        #array.append(2)
        array=[1,2,3,4]
        print(array)
    return a
arr = [1]
aa=c(arr)
aa()
print(arr)
