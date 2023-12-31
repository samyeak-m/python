import pandas as pd

test=pd.read_csv(r'data.csv',encoding='unicode_escape')
# print('\n5 rows:\n',test)
# print('\nall of data\n',test.to_string())
# print('\nfirst 5 rows:\n',test.head())
# print('\nlast 5 rows:\n',test.tail())
# print('\ndetail info:\n',test.info())
# print(pd.options.display.max_rows)
# pd.options.display.max_rows=75
# print(pd.options.display.max_rows)

# never work on orginalfile
# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# # print('\nwithout dropna\n',df.to_string())
# new_result=df.dropna()
# # print('\nwith dropna(blank and duplicate data is remove):\n',new_result.to_string())
#
# df.dropna(inplace=True)
# print('\nwith dropna\n',df.to_string())

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# df.fillna(100,inplace=True)
# print('\nwith fillna\n',df.to_string())

df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# print('\nwithout fillna\n',df.to_string())
# print(df.info())
df['Calories'].fillna(50,inplace=True)
print('\nwith fillna\n',df.to_string())