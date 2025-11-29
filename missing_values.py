import numpy as np
a=np.array([1,2,3,4,np.nan,6])#np.nan--> create missing values
print(a)
x=np.isnan(a)#np.isnan-->search for missing values
print(x)
#now invert it so that we can find values that are not missing
y=a[~np.isnan(a)]
print(y)