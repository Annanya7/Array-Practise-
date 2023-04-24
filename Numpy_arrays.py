from numpy import * 
a=array([[1,2,3,4],
        [5,6,7,8],
        [8,9,10,11]])
print(a)
print(a.ndim)
print(a.shape)
a.shape=(4,3)
print(a)
print(a.size)
print(a.itemsize)
print(a.nbytes)
