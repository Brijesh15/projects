def fruits():
    yield "Mango"
    yield "Jackfruit"
    yield "Banana"
    yield "Guava"

getfruits = fruits()
for fruit in getfruits:
    print(fruit)
