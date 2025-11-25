import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
#============
#  INDEXING. ||
#============
#1d indexing works same as in python(0 based indexing and negative based indexing)
print(a2)
#2d [row , column]==>for 6 a2[1,2]
a=a2[1,2]
print(a)


#3d==>3d is always made of 2d
#first find how many 2d are there in 3d
print(a3)
#3d [which 2d,row of 2d,column of 2d]==> for 5 a3[1,0,1]
b=a3[1,0,1]
print(b)

#similar in 4d and so on......

#==================
#.  SLICING.    |||
#==================
#1d==>a1[start:end:increment/decrement]==>end is not included
#2d
print(a2)
#a2=[[ 0  1  2  3]
 #   [ 4  5  6  7]
#    [ 8  9 10 11]]

#for first row in 2d array we can write a2[0,:] as we need row at 1 and all columns are included
c=a2[0,:]
print(c)

#for third column in 2d array a2[:,2]
d=a2[:,2]
print(d)

#for 5,6 & 9,10==>a2[1:,1:3]==>row-->1 onwards,column-->1onwards 3-->means after 1 and 3rd column is not excluded
x=a2[1:,1:3]
print(x)

#for 0,3,8,11 ==>a2[::2,::3]==>one : for 0 onwards all-->means all rows && one : for increment/decrement
#as for above case we need rows 1 and 3 && column 1 and 4
#so first we include all rows and column 
#and then we give increment of 2 in rows to jump from 1 to 3
#and similarly for column we give incrment of 3 to jump from 1 to 4
y=a2[::2,::3]
print(y)

#similarly for 1 ,3,9,11==>a2[::2,1::2]
z=a2[::2,1::2]
print(z)

#similarly for 4 and 7
s=a2[1:2,::3]

print(s)
#or
d=a2[1,::3]
print(d)

#for 1,2,3,5,6,7
e=a2[:2,1:]
print(e)

#3d
a4=np.arange(27).reshape(3,3,3)
print(a4)
#a4=[[[ 0  1  2]
 #    [ 3  4  5]
  #.  [ 6  7  8]]

 #.  [[ 9 10 11]
  #.  [12 13 14]
  #.  [15 16 17]]

 #   [[18 19 20]
 #    [21 22 23]
 #    [24 25 26]]]
#for 2nd 2d
f=a4[1]
print(f)
####doubt==>we can access in 3d by index then why we are unable to do so in 2d
#for alternate 2d
g=a4[::2]
print(g)

#for 1st 2d 2nd row
h=a4[0,1]
print(h)

#for 
# 2nd 2d middle column
i=a4[1,:,1]
print(i)

#for 22,23,25,26
j=a4[2,1:,1:]
print(j)

#for 0,2,18,20
k=a4[::2,0,::2]
print(k)