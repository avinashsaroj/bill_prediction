import pandas as pd

data=pd.read_excel('electricity_bill2.xlsx')
print(data)
'''
#data.columns=['Year','Month','Amount']
data['Year']=[2020,2020,2020,2020,2020]
data['Month']=[8,9,10,11,12]
data['Amount']=[0,0,0,0,0]

print(data)

print(data.info())

data.to_excel('test_again.xlsx')'''