import os
path = os.path.dirname(os.path.abspath(__file__))
print(path)
import ctypes
NUM = 20
fun = ctypes.CDLL("libfun.so")
fun1 = fun.myFunction
fun1.argtypes = (ctypes.c_int,)
fun1.restype = ctypes.c_int
#fun.myFunction.argtypes()
returnVale = fun.myFunction(NUM)
print(returnVale)
