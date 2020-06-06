def producer(sentance,pf):
    print("I am producer")
    tokens = sentance.split(" ")   
    print("split_output:",tokens) 
    for item in tokens:
        pf.send(item)
    pf.close()

def p_filter(pattern="brijesh",nt=None):
    print("I am pattern filter")
    try:
        while True:
            token = (yield)
            if token:
                nt.send(token)
    except GeneratorExit:
           print("done with filtering")

def print_token():
    print("I am print token")
    try:
        while True:
            token = (yield)
            print("Token:",token)
    except GeneratorExit:
           print("done with printing")

if __name__ == "__main__":
    pt = print_token()
    pt.__next__()
    pf = p_filter(nt=pt)
    pf.__next__()

    sentance = 'Bob is running behind a fast moving car'
    producer(sentance,pf)
