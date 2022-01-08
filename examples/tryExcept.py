def A():
    try:
        print("try")
        return 1
    except: 
        print("except")
        return 2
    else:
        print("else")
        return 3
    finally:
        print("finally")
        return 4

print(A())
