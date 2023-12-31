import pandas as pd

test=pd.read_csv('data.csv',encoding='unicode_escape')
# print('\n5 rows:\n',test)
# print('\nall of data\n',test.to_string())
# print('\nfirst 5 rows:\n',test.head())
# print('\nlast 5 rows:\n',test.tail())
# print('\ndetail info:\n',test.info())
print(pd.options.display.max_rows)
pd.options.display.max_rows=75
print(pd.options.display.max_rows)
