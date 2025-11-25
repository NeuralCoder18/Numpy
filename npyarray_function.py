import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)

#max/min/sum/prod
a=np.max(a1)       #same min,sum and prod
print(a1)
print(a)

#if we want min of each row
#0-->col and 1-->row
b=np.min(a1,axis=0)
print(b)

#mean/median/std/var
np.mean(a1)        #same median/std/var
np.mean(a1,axis=1)

#trigonometric functions
a=np.sin(a1)
print(a)


#dot product(no of column of first matrix=no of rows of second matrix)
a2=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(3,4)
np.dot(a2,a3)

#log and exponents
np.log(a1)
np.exp(a1)


#round/floor/ceil
#round-->round off to nearest integer
#floor-->back to piche wala integer as 6.9-->6 
#ceil-->aage wala integer as6.1-->7
