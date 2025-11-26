import numpy as np
#horizontal stacking
#[2x2] [2x2]-->stack horizontally-->[2x4]
#vertical stacking
##[2x2] [2x2]-->stack vertically-->[4x2]
#shape should be same
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
#hstack
a=np.hstack((a4,a5))
print(a)

#vstack
b=np.vstack((a4,a5))
print(b)
