# to install numpy : pip install numpy

import numpy as np
a=np.array([2,3,5,7,9])
print(a)
print(type(a))
print("\nversion of numpy : ",np.__version__)

test=np.array([1,2,3,4,5])
print("\ntuple convert into array : ",test)

test1=np.array(10)
print("\nzero dimensional arraay/1-D : ",test1)

test2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\n2-D : ",test2)

test3=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print("\n3-D : ",test3)

# ndim to check the dimension of array
print("\ntest is ",test.ndim," dimensional")
print("test1 is ",test1.ndim," dimensional")
print("test2 is ",test2.ndim," dimensional")
print("test3 is ",test3.ndim," dimensional")

# ndmin is used to convert the dimension of array
test5=np.array([1,2,3,4,5],ndmin=5)
print("\n5-D : ",test5)
print("test5 is ",test5.ndim," dimensional")

z=np.array([1,2,3,4,5,6,7])
print("\n",z[0])
print(z[2]+z[3])

z1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\n",z1[1,1])

z2=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
print("\n",z2[0,1,2])
print(z2[1,1,2])
