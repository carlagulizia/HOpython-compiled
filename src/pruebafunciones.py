import ctypes as C
math = C.CDLL('./libmath.so')
tres = C.c_float(3)
cuatro = C.c_float(4)
res = C.c_float()
math.add_float_ref(C.byref(tres),
                   C.byref(cuatro),
                   C.byref(res))

