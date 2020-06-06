# Python3 program for demonstrating 
# coroutine execution
def print_name(prefix):
    try:
        print("Searching prefix:{}".format(prefix))
        while True:
            name = (yield)
            print("sent data:",name)
            if prefix in name:
                print(name)
    except GeneratorExit:
               print("Closing coroutine") 
    except StopIteration:	  
         print("sending data after Closing coroutine") 
#    else:
#        print("else statement")
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and 
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
corou.__next__()
 
# sending inputs
#corou.send("Atul")
corou.send("Dear Atul")
corou.close()
corou.send("Dear Brijesh")
