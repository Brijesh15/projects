import copy

list1 = ['a','b','c','d']

print "simple copy"
#list2 = copy.copy(list1)
list0 = list1
list0[1]='e'
print list1
print list0

print "shallo copy"
list2 = copy.copy(list1)
list2[1]='f'
print list1
print list2

print "deep copy"
list3 = copy.deepcopy(list1)
list3[1]='f'
print list1
print list3

