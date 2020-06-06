def pipeline(*funcs):
    def helper(arg):
        res=0
        for fun in funcs:
            g = fun
            if res == 0:
                res = g(arg)
                continue
            res=g(res)
        return res
    return helper
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0
