# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:08:04 2018

@author: abhis
"""

import requests


class NewClass():
    
    def dw(self,image_url,save):
        
        #image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
        r = requests.get(image_url) # create HTTP response object 
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open(save,'wb') as f: 
            # Saving received content as a png file in 
            # binary format   
            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 
        print('File downloaded, Check directory')
        

if __name__=="__main__":
    n=NewClass()
    url=str(input('Enter url of file to be downloaded : '))
    saveas=str(input('What name do you want it to be stored as : '))
    n.dw(url,saveas)