import copy
def chaotic(array_len, array):
    orig_list = copy.deepcopy(array)
    orig_list.sort()
    count = 0
    chaoticCount = 0
    for i in range(array_len):
        if orig_list[array_len - (i+1)] == array[array_len - (i+1)]:
            chaoticCount = 0
            continue
        chaoticCount+=1
        if chaoticCount == 3:
            return "too choatic"
        temp = orig_list[array_len - (i+1)]
        orig_list[array_len - (i+1)] = orig_list[array_len - (i+2)]
        orig_list[array_len - (i+2)]  = temp
        count+=1
    return count

print(chaotic(5, [2,1,5,3,4]))
print(chaotic(5, [2,5,1,3,4]))


