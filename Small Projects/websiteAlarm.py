# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 01:53:00 2018

@author: abhis
""" 

import time 
import webbrowser 

def getData():
    Set_Alarm = input("Set the website alarm as H:M:S:") 
    url = input("Enter the website you want to open:") 

    Actual_Time = time.strftime("%I:%M:%S")
    #print(Actual_Time) 
    if(Set_Alarm<Actual_Time):
        print('Wrong time entered')
        main()
        
    return Set_Alarm,Actual_Time,url

def Alarm(Set_Alarm,Actual_Time,url):
    while (Actual_Time != Set_Alarm): 
        #print("The time is " + Actual_Time)
        Actual_Time = time.strftime("%I:%M:%S") 
        time.sleep(1) 
    
    
    if (Actual_Time == Set_Alarm): 
        print("You should see your webpage now :-)")
        webbrowser.open(url)
 
def main():
    Set_Alarm,Actual_Time,url=getData()
    Alarm(Set_Alarm,Actual_Time,url)

main()
