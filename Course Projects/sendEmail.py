# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:10:11 2018

@author: abhis
"""

# Python code to illustrate Sending mail from  
# your Gmail account 

#will need to turn on allow less secure apps in google account settings
 
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sender email id", "##############") 
  
# message to be sent 
message = "Message sent from Python program"
  
# sending the mail 
s.sendmail("sender email id", "receiver email id", message) 
  
# terminating the session 
s.quit() 