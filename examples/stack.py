from ctypes import *
import ctypes

dll = CDLL('test.so')
test1 = dll.testfun1
test1.argtypes = c_double,POINTER(ctypes.c_wchar),c_char_p
test1.restype = c_double

a = 2.5
b = (ctypes.c_wchar * 5)()  # create an array of three doubles
print("b",b)
s = b'test123'
#b[4]= 'c'
print("b",b)
d = test1(a,b,s)
print(d,list(b))
