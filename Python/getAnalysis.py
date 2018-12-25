# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 22:38:56 2018

@author: abhis
"""

import csv
import pandas as pd
import numpy as np

data_xls = pd.read_excel('applications.xlsx', index_col=None)
data_xls.to_csv('new.csv', encoding='utf-8',index=False)

x=pd.read_csv('new.csv')
a,b=x.shape
count=0
new=np.array(x).reshape(a,b)

for i in range(0,new.shape[0]):
    k=5
    j=0
    y=str(new[i][5])
    x=str(y.lower())
    if(x=='reject' or x[0:2]=='ha'):
        count+=1

print('Rejects are : {}'.format(count))
rem=int((a-count)*0.8)
print('Yet to reply are approximately : {} '.format(rem))


#print(new[0][6])
#print(x[:][:])