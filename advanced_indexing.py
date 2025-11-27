import numpy as np

a1=np.arange(12).reshape(4,3)
#====================
#.   FANCY INDEXING ||
#====================
#a1=[[ 0  1  2]
#    [ 3  4  5]
#    [ 6  7  8]
#    [ 9 10 11]]

#for 1st 3rd and 4th
#when there is no pattern we use fancy indexing
#in fancy indexing we can provide a list of row or column which we need
#a1[[0,2,3]]
a=a1[[0,2,3]]
print(a)

a2=np.arange(24).reshape(6,4)
#a2=[[ 0  1  2  3]
    #[ 4  5  6  7]
    #[ 8  9 10 11]
    #[12 13 14 15]
    #[16 17 18 19]
    #[20 21 22 23]]

# for 1st 3rd 4th and 6th row

b=a2[[0,2,3,5]]
print(b)

#for 1st 2nd and 4th column
c=a2[:,[0,1,3]]
print(c)


#=========================
#.    BOOLEAN INDEXING ||| super important
#=========================
a3=np.random.randint(1,100,24).reshape(6,4)

#find all numbers greater than 50
print(a3[a3>50]) #a3>50 gives boolean array and when we paste in a3 it prints the value where true occurs

#find all number greater than 50 and are even
print(a3[(a3>50) & (a3%2==0)])

#find all numbers not divisible by 7
print(a3[a3%7!=0])

