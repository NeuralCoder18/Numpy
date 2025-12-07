import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
#np.sort
#Return a sorted copy of an array
x=np.sort(a)#for descending order we have to use [::-1]after x
print(x)
y=np.sort(b)#-->row wise sorting.For column wise sorting np.sort(b,axis=0)
print(y)

#np.append
#the numpy.append() appends values along the mentioned axis at the end of the array
z=np.append(a,200)
print(z)

c=np.append(b,np.ones((b.shape[0],1)),axis=1)
print(c)

#np.concatenate
#numpy.concatenate() function concatenate a sequence of arrays along an existing axiss.
aa=np.arange(6).reshape(2,3)
bb=np.arange(6,12).reshape(2,3)
cc=np.concatenate((aa,bb),axis=0)   #used in place of vertical stack
print(cc)
dd=np.concatenate((aa,bb),axis=1)
print(dd)

#np.unique
#with the help of np.unique() method,we can get the unique values from an array given as parameter in np.unique() method
e=np.array([1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5])
print(np.unique(e))

#np.expand_dims
#with the help of Numpy.expand_dims(), we can get the expanded dimensions of an array )
f=np.expand_dims(a,axis=1)
print(f)

#np.where
#the numpy.where() function returns the indices of elements in an input array where the given condition is satisfied

#find all indices with value greater than 50
print(np.where(a>50))
#replace all values >50 with 0 -->np.where(a>50,true,false) ==>if true -->replace by given value at place of true

print(np.where(a>50,0,a))

#np.argmax
#The numpy.argmax() function returns inices of the max element of the array in a particular axis
print(np.argmax(a))
print(b)
print(np.argmax(b,axis=0))

#np.argmin--> same

#np.cumsum
# numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis
print(np.cumsum(a))
print(np.cumsum(b,axis=0))# if you dont give axis it will convert it to 1d and then perform cummulative sum

#np.cumprod
#np.cumprod() function is used when we want to compute the cumulative product of array elements over a given axis
print(np.cumprod(a))

#np.percentile 
#numpy.percentile() function is used to compute the nth percentile of the given data(array elements) along the specified axis
print(np.percentile(a,100))

#np.histogram
#give frequency of numbers present between a bin size
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))

#np.corrcoef
#Return Pearson product-moment correlation coefficient
# generally correlation between -1 to 1==>if two data are correlated by 1 it means if one data increase second data also increases
salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience))

#np.isin
#with the help of numpy.isin() method,we can see that one array having values are checked in a different numpy array having different 
#elements with different sizes==>can be used for multiple items
items=[10,20,30,40,50,60,70,80,90,100]
print(np.isin(a,items))
print(a[np.isin(a,items)])

#np.flip
#the numpy.flip() function reverses the order of an array elements along the specified axis,preserving the shape of the array
print(a)
print(np.flip(a))
print(b)
print(np.flip(b))#==>it flips rowwise as well as column wise if we dont give axis

#np.put
#The numpy.put function replaces specific elements of an array with given values of p_array.Array indexed works on flattened array.
print(np.put(a,[0,1],[110,530]))#==>do permanent changes
print(a)

#np.delete()
#The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis 
print(np.delete(a,0))

#Set functions
#==>np.union1d
#==>np.intersect1d
#==>np.setdiff1d
#==>np.setxor1d-->remove common of both array
#==>np.in1d

#np.clip
#numpy.clip() function is usedto clip(limit) the values in array
#np.clip(a,a_min=,a_max=)
print(np.clip(a,a_min=25,a_max=75))

#np.swapaxes
#np.uniform
#np.count_nonzero

