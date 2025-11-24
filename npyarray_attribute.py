import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)



#ndim(gives dimension of array)
a=a3.ndim

print(a)

#shape
#i.e. tells about rows and columns
a=a2.shape
print(a)

#size(tells how many items )
a=a3.size
print(a)

#itemsize(int32=4byte,int64=float=8byte)
a=a2.itemsize
print(a)

#dtype(tells datatype )
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
