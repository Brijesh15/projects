x,y = 1,1
def f():
    global x
    y=0
    for i in (10,20,30):
        x+=1
        y+=1
f()
print x,y
