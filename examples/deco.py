# Adds a welcome message to the string
# returned by fun(). Takes fun() as
# parameter and returns welcome().
from functools import wraps
def decorate_message(fun):
 
    # Nested function
    print('I am a decorate_message')
    #@wraps(fun)
    #def wrapper(site_name):
    def addWelcome(site_name):
        print("+++",site_name)
        return "Welcome to " + fun(site_name)
 
    # Decorator returns a function
    return addWelcome
    #return wrapper
#print(decorate_message(site('GeeksforGeeks'))) 
@decorate_message
def site(site_name):
    print("I am site function")
    return site_name;
#print(decorate_message(site('hh')))
 
# Driver code
 
# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
#print(decorate_message(site('GeeksforGeeks')))
print(site("GeeksforGeeks"))
print site.__name__
