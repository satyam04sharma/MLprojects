import numpy as np
import sklearn as sk
import os
arr=np.array([[1,2,3],[1,3,4]])
print(arr)
m=np.random.rand(4,4)
print(m)
m=np.mat(m).I
print(m)
x=np.eye(4)
print(m-x)