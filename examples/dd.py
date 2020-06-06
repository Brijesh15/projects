def smart_divide(name):

    def check(function):
        def inner(a,b):
            print("I am going to divide",a,"and",b)
            if b == 0:
                print("Whoops! cannot divide")
                return

            return function(a,b)
        return inner
    print "name:-",name
    return check

@smart_divide('brijesh')
def divide(a,b):
    print "printing from decorator"
    return a/b
#smart = smart_divide(divide)
#print smart()
print divide(2,5)
