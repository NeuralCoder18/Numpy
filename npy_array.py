import numpy as np
#declairing 1d array
a=np.array([1,2,3,4])
print(type(a))
print(a)

#creating 2d and 3d array
b=np.array([[1,2,3],[4,5,6]])
print(b)

c=np.array([[1,2],[3,4],[5,6]])
print(c)

#dtype
# (you can create array of datatype according to you )
#for float/bool/complex.....
d=np.array([1,2,3,4],dtype=float)
print(d)

#np.arange
#=================
#. works as range function in python
#=================
#np.arange(a,b,c)
#a=start(included) b=end(excluded) c=increment/decrement
a=np.arange(1,11)
print(a)

# reshape(i.e. converts 1d array in 5x2 matrix in below example)
b=np.arange(1,11).reshape(5,2)
print(b)
#==========================
# DEFAULT DATATYPE IS FLOAT
#==========================

#np.ones and np.zeros
#np.ones(creates an array of axb in which every element is 1)
c=np.ones((3,4))   #(creates matrix of 3 rows 4 columns)
print(c)

#similar np.zeros with every element 0
d=np.zeros((3,4))
print(d)
#Replace with “np.random is a module, and np.random.random() is a function that returns random floats in [0,1)”
#=================================================================
# USING TWO RANDOM BECAUSE ONE RANDOM IS CLASS AND OTHER IS METHOD
#=====================================================================
#np.random(generates random number b/w 0 and 1 and rows columns are same as np.ones)
a=np.random.random((3,4))
print(a)


#np.linspace(linearlyspace)
#(generates points at equal distance b/w two points)
#np.linspace(a,b,c)
#a=lower range ;b=upper range;c=number of item you want b/w lower and upper range
b=np.linspace(-10,10,10)
print(b)


#np.identity(by usingthis we can create identity matrix)
#np.identity(a)==>a=order
c=np.identity(3)
print(c)