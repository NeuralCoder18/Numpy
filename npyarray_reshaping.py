import numpy as np
a2=np.arange(12).reshape(3,4)
#reshape
#transpose==>same as matrix
#used as np.transpose(a2)//a2.T
#ravel
#not permanent
#transpose
a=np.transpose(a2)
print(a)

#==>converts the array to 1d
b=a2.ravel()
print(b)
