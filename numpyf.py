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

# array slicing
messi=np.array([1,2,3,4,5,6,7,8,9,10])
print("\nindex stat from 1 and end at 5 : ",messi[1:5])
print("index start from 1 and end at 7 with step 2 : ",messi[1:7:2])

neymar=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\n",neymar)
print(neymar[0,1:4])
print("here is : ",neymar[0:3,1])
print("here is another one : ",neymar[0:2,0:3])

# Negative silcing
squarez=np.array([1,2,3,4,5,6,7,8,9,10])
print("\n",squarez[-5:-1])
print(squarez[-4:])
print("returns every values : ",squarez[::])

# aithmetic co operation
array1=np.array([1,2,3,4,5])
array2=np.array([4,3,2,1,10])
sum=np.add(array1,array2)
print("\nsum of array : ",sum)
print("subtract : ",np.subtract(array1,array2))
print("multiple : ",np.multiply(array1,array2))
print("divide : ",np.divide(array1,array2))
print("power : ",np.power(array1,array2))
print("remainder : ",np.remainder(array1,array2))
print("mod 1 of 2: ",np.mod(array1,array2))
print("mod 2 of 1 : ",np.mod(array2,array1))

messi=np.array([1,2,3,4,5])
suraz=np.array([6,7,8,9,10])
print("\n",divmod(messi,suraz))

array3=np.trunc([1.2,2.3,3.4,4.5,5.6])
array4=np.fix([1.2,2.3,3.4,4.5,5.6])
print("\n",array3)
print(array4)

print("\n",sum)
result=np.sum([array1,array2],axis=1)
print("\nsum on axis 1 : ",result)
result=np.sum([array1,array2],axis=0)
print("\nsum on axis 2 : ",result)

result=np.cumsum([array1,array2])
print("\ncumsum : adding and printing one array at a time : ",result)

# data-type

messi=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("\ndata type : ",messi.dtype)

neymar=np.array(['N','E','PEPAL','a','l'],dtype='S')
print("\n",neymar)
print(neymar.dtype)

test=np.array([1,2,3,4,5],dtype='i4')
print("\n",test)
print('here is : ',test.dtype)

# test=np.array(['a',1,2,3],dtype='i4')
# print("\n",test)
# # print("here again",test.dtype)

test1=np.array([1.0,2.1,3.1])
test2=test1.astype('i')
print("\nfinal : ",test2)
print(test2.dtype)

test1=np.array([2,0,4,0,6])
test2=test1.astype(bool)
print("\nfinal : ",test2)
print(test2.dtype)

suarez=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\nnumber and size of array : ",suarez.shape)

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("\n",a)
b=a.reshape(4,3)
print("\nreshaping a to 2d (4,3) : \n",b)

c=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d=c.reshape(2,3,2)
print("\nreshaping c to 3d(2,3,2) : \n",d)

# random

from numpy import random as rd
x=rd.randint(50)
print("\n",x)

y=rd.rand()
print("\n",y)

z=rd.randint(100,size=(5))
print("\n",z)

a=rd.randint(100,size=(3,5))
print("\n",a)

l=rd.randint(100,size=(2,3,5))
print("\n",l)

m=rd.rand(4)
print("\n",m)

o=rd.choice([4,5,6,23,56])
print("\n",o)

p=rd.choice([4,5,6,23,56],size=(2,3))
print("\n",p)

arr =rd.choice([4,5,6,23,56],p=[0.1,0.3,0.2,0.4,0.0],size=(100))
print("\n",arr)

# view and copy

array1 = np.array([1,2,3,4,5])
array2 = array1.copy()
array2[0]=90
print("\n",array1)
print(array2)

array1 = np.array(['a','b','c','d','e'])
array2 = array1.copy()
array2[0]='z'
print("\n",array1)
print(array2)

array3 = array1.view()
array1[0]='n'
print("\n",array1)
print(array3)

e=np.array([1,2,3,4,5,6,7,8])
print("\n",e.reshape(2,4).base)

arr3=np.array([1,2,3,4,5,6,7,8])
for x in arr3:
    print(x)

for x in np.nditer(arr3):
    print('nditer',x)

for idx,x in np.ndenumerate(arr3):
    print(idx,x)