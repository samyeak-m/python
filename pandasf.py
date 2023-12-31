import pandas as pd

print('pandas version : ',pd.__version__)

dataset={
    'cars':['BMW','Volvo','Ford'],
    'mydata':[3,7,2]
}

print(dataset)
result=pd.DataFrame(dataset)
print("\n",result)

x=[1,2,3,9]
result=pd.Series(x)
print("\n",result)

print(result[1])

result2=pd.Series(x,index=['a','b','c','d'])
print("\n",result2)

print(result2['c'])

student={
    'first_name':'Lionel',
    'last_name':'Messi',
    'age':36,
    'address':'Rosario'
}

result3=pd.Series(student)
print("\n",result3)

test=pd.Series(student,index=['last_name','address'])
print("\n",test)

marks={
    'Subject':['Pyhysics','Chemistry','Maths'],
    'Marks':[90,80,70]
}

test1=pd.DataFrame(marks)
print("\n",test1)
test2=pd.Series(marks)
print("\n",test2)

print('\nin series\n',test1.loc[0])
print('\nin datafrom\n',test1.loc[[0,1]])

result3=pd.DataFrame(marks,index=['first','second','third'])
print("\n",result3)
print('\nin datafrom\n',result3.loc[['second','third']])