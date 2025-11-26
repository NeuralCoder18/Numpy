import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)


#1d 
for i in a1:
    print(i)

#2d
for i in a2:
    print(i) # ==>print a row every time

#3d
for i in a3:
    print(i)   #==>print a 2d array every time


#for iteration through each element we can write==>this first convert 3d array to 1d array then print each element
#it is for all dimension array
for i in np.nditer(a3):
    print(i)