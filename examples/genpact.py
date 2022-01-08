def deco(func):
    def wrap(*args, **kwargs):
        print("before calling fuction")
        func()
        print("after calling fuction")
    return wrap



@deco
def hello():
    print("hello")

hello()
