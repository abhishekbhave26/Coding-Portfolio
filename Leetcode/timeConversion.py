# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:07:36 2018

@author: abhis
"""
#convert time from 12hr to 24hr

def timeConversion(s):
    
    n=len(s)
    ampm=s[n-2:n]
    if(ampm=='PM'):
        pm=int(s[0:2])
        rest=s[2:n-2]
        if(pm==12 and s[3:5]=='00' ):
            pm='00'
            return pm+rest
        elif(pm==12 and s[3:5]!='00'):
            return s[0:n-2]
        pm+=12
        pm=str(pm)
        return pm+rest
        
    else:
        am=int(s[0:2])
        rest=s[2:n-2]
        if(am==12):
            am='00'
            return am+rest
        if(am<10):
            
            am='0'+str(am)
            
        am=str(am)
        return am+rest
        
        
    
print(timeConversion('12:45:54PM'))