def m(e):
    e.append("foo")
    e = ["bar","baz"]
a = ["a"]
m(a)
print(a)

def f():
    values = []
    def widget(v):
        values.append(v)
        return values
    return widget

worker = f()
worker(1)
worker(2)
print(worker(3))
