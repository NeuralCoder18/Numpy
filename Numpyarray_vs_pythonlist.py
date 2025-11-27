import numpy as np
import time
import sys
#===============
#   SPEED |||
#==============

#list
# a=[i for i in range(10000000)]
# b=[i for i in range(10000000,20000000)]
# c=[]
# start=time.time()
# for i in range (len(a)):
#     c.append(a[i]+b[i])
# print(time.time()-start)

#numpy
# a=np.arange(10000000)
# b=np.arange(10000000,20000000)
# start=time.time()
# c=a+b
# print(time.time()-start)

#Because NumPy operations run in optimized C loops, while Python lists run in slow Python for-loops.

#===============
#   MEMORY
#==============
#list
# a=[i for i in range(10000000)]
# print(sys.getsizeof(a)).    # Only returns size of list object, not elements

#memory
# a=np.arange(10000000,dtype=np.int32) #numpy gives you flexibility to work with size of number according to you
# print(sys.getsizeof(a))
#print(a.nbytes) sys.getsizeof(a) does not give correct memory for NumPy arrays because it only shows the size of the Python object, not the underlying array buffe


#================
#. CONVENIENCE ///
#================
#numpy is more convenient than python list
# NumPy is more convenient than Python lists because it supports vectorized operations.
# Example: c = a + b (no loops!)
