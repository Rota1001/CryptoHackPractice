import numpy as np

def GaussianReduction(v1, v2):
    while True:
        if v2.dot(v2) < v1.dot(v1):
            v1, v2 = v2, v1
        m = v1.dot(v2) // v1.dot(v1)
        if m == 0:
            return v1, v2
        v2 -= m * v1
    

v = np.array([846835985, 9834798552], dtype='i8')
u = np.array([87502093, 123094980], dtype='i8')

x, y = GaussianReduction(v, u)
print(x.dot(y))
