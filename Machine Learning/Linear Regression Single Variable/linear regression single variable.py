# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:30:43 2018

@author: abhis
"""


#given height of father predict height of son

# reading dataset
import pandas as pd

#mathematical computation 
import numpy as np

#plot graph
from matplotlib import pyplot as plt

#linear regression model
from sklearn.linear_model import LinearRegression


#import csv file

#df=pd.read_csv('father_son.csv',delim_whitespace=True,header=None,dtype=np.float64)
#prints first 10 rows
#print(df.head(10))


# prepare training data


#x=people.father_stature
#y=people.son_stature
#x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1)


#x_train=df.iloc[2:,0:1].values
#y_train=df.iloc[2:,1:2].values
x_train=[[65.8]
,[67.7]
,[60.7]
,[63.1]
,[64.1]
,[68.3]
,[62.9]
,[62.7]
,[63.6]
,[63.6]
,[63]
,[64.9]
,[64.4]
]

y_train=[[60.8]
,[61.9]
,[62.4]
,[62.7]
,[62.6]
,[62.8]
,[63.5]
,[63.8]
,[63.6]
,[63.8]
,[63.4]
,[63.6]
,[63.5]
]


#train the model 
lm=LinearRegression()
lm.fit(x_train,y_train)



#test the model
no=[[68.5],[65.1],[70.2],[63.5]]
predictions=lm.predict(no)
print(predictions)

#plot the best fit line
plt.scatter(x_train,y_train,color='b')

plt.plot(no,predictions,color='black',linewidth=3)
plt.xlabel('Father height in inches')
plt.ylabel('Son height in inches')
plt.show()


