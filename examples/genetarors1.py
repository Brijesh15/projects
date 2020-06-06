def my_gen():

    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
	print item    

print "reverse a string"
def rev_str(my_str):
   	length = len(my_str)
    	for i in range(length -1,-1,-1):
        	yield my_str[i]

for char in rev_str("hello"):
     	print(char)

my_list = [1, 3, 6, 10]

a= ( x**2 for x in my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
#next(a)

