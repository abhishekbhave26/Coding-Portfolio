# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:57:20 2018

@author: abhis
"""

def listComprehension():
    company=['1 HAL','2 Sukhoi','3 Dassualt']
    plane=['1 Tejas','2 Su 30 Mki','3 Rafale']
    combination=[(x,y) for x in company for y in plane if x[0]==y[0]]
    print(combination)

def FtoC():
    
    Celsius = [39.2, 36.5, 37.3, 37.8]
    Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius if x>37 ]
    print(Fahrenheit)
    
listComprehension()
FtoC()