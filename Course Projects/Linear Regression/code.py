# import libs
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

#import data 

df=pd.read_csv('treeing.csv',delim_whitespace=True)

#prepare data for training

x_train=df['time'].values[:,np.newaxis]
y_train=df['value'].values

# train the model

lm=LinearRegression()
lm.fit(x_train,y_train)

#prepare test data
x_test=[[1990],[2000],[2008],[2018],[2030]]

predictions=lm.predict(x_test)
print(predictions)

#plot
plt.scatter(x_train,y_train,color='b')

plt.plot(x_test,predictions,color='black',linewidth=3)

plt.xlabel('Years')
plt.ylabel('Tree value')
plt.show()