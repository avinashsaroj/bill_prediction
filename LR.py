import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_excel('electricity_bill2.xlsx')
test_data=pd.read_excel('test_again.xlsx')
print(test_data)
#print(data)
x=data[['Year','Month']]
y=data[['Amount']]
test_x=test_data[['Year','Month']]
#print(test_x)
test_y=test_data[['Amount']]

from sklearn.linear_model import LogisticRegression

logmodel=LogisticRegression()
logmodel.fit(x,y)

#logmodel.fit(test_x,test_y)

prediction=logmodel.predict(test_x)
print(prediction)
















