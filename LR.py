import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel('electricity_bill.xlsx')
print(data.head())

#sns.heatmap(data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#plt.figure(figsize=(10,10))
#sns.boxplot('Units','Month',None,data)


x=data.iloc[:,:-1]
y=data.iloc[:,3]
month=pd.get_dummies(x['Month'],drop_first=True)
x= x.drop('Month',axis=1,inplace=True)
x=pd.concat([x,month],axis=1)
print(x.head())

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(data.drop('Amount',axis=1),data['Amount'],test_size=0.30,random_state=101)

from sklearn.linear_model import LinearRegression

logmodel=LinearRegression()
logmodel.fit(x_train,y_train)

prediction=logmodel.predict(x_test)
print(prediction)

from sklearn.metrics import confusion_matrix

accuracy=confusion_matrix(y_test,prediction)
print(accuracy)



















#plt.show()
