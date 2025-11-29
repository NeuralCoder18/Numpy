import numpy as np
#Working with mathematical formula

#sigmoid
#sigmoid of x=1/1+e^-x
a=np.arange(10)
def sigmoid(array):
    return 1/(1+np.exp(-(array)))

print(sigmoid(a))


#mean squared error 
#(original-prediction )^2
actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
def mse(actual,predicted): 
    return np.mean((actual-predicted)**2)
print(mse(actual,predicted))   