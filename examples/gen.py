def Generator():
    i = 1
    while True:
        yield i*i
        i = i+1


for item in Generator():
    if item > 100:
        break
    print item
