import numpy as np
#horizontalsplitting-->reverse of hstacking


#vertical splitting-->reverse of v stacking


a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)

#hsplit-->np.hsplit(array,no of parts in which you want to split but it should be in equal parts)
a=np.hsplit(a4,2)
print(a)

#vsplit-->np.vsplit(array,no of parts in which you want to split)
b=np.vsplit(a5,3)
print(b)