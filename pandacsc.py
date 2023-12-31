import pandas as pd

# test=pd.read_csv(r'data.csv',encoding='unicode_escape')
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

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# print('\nwithout fillna\n',df.to_string())
# print(df.info())
# df['Calories'].fillna(50,inplace=True)
# print('\nwith fillna\n',df.to_string())

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# mean_value=df['Calories'].mean()
# print('mean is : ',mean_value)
# df['Calories'].fillna(mean_value,inplace=True)
# print('\nfillna with mean\n',df.to_string())

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# median_value=df['Calories'].median()
# print('median is : ',median_value)
# df['Calories'].fillna(median_value,inplace=True)
# print('\nfillna with median\n',df.to_string())

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# mode_value=df['Pulse'].mode().iloc[0]
# print('mode is : ',mode_value)
# df['Pulse'].fillna(mode_value,inplace=True)
# print('\nfillna with mode\n',df.to_string())

# df=pd.read_csv(r'data.csv',encoding='unicode_escape')
# # print(df.to_string())
# df['Date']=pd.to_datetime(df['Date'])
# print('\ndate formating\n',df.to_string())

df=pd.read_csv(r'data.csv',encoding='unicode_escape')
df.dropna(subset=['Date'],inplace=True)
print('\nwith dropna\n',df.to_string())
print(df.dtypes)