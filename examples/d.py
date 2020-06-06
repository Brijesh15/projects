import copy
def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    numlist = copy.deepcopy(numbers)
    numlist.pop(0)
    for i in numbers:
        print(i, numlist)
        for j in numlist:
            if (i+j) == target_sum:
                return (numbers.index(i),numbers.index(j))
                #print(numbers.index(i),numbers.index(j))
        try:
            numlist.pop(0)
        except:
            return "none"
    return None

print(find_two_sum([0,-1, -2, 5, 7, 5, 9], 10))
