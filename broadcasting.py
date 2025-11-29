import numpy as np
## the term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations.
# the smaller array is "broadcast" across the larger array so that they have compatible shapes.
#===========
#same shape
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)

print(a)
print(b)
print(a+b)

#Different Shape
a1=np.arange(6).reshape(2,3)
b1=np.arange(3).reshape(1,3)

print(a)
print(b)
print(a+b) 
 
 #=============================
 #     Broadcasting Rules
 #=============================

 #1-->Make the two arrays have the same number of dimensions.
 #.   :if the numbers of dimensions of the two arrays are different,add new dimensions with size 1 to the head of the array with the smaller dimension 

 # 2-->Make each dimension of the two arrays the same size.
 #    :if the sizes of each dimension of the two arrays do not match,dimension with size 1 are stretched to the size of the other array.
 #.   :if there is a dimension whose size is not 1 in either of the two arrays , it cannot be broadcasted,and an error is raised.



    