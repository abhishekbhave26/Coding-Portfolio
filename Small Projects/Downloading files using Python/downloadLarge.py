# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:10:50 2018

@author: abhis
"""

import requests

class New():
    
    def dw(self,file_url,save):
    
        #file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
        r = requests.get(file_url, stream = True) 
        #x=file_url.split
        #print(x)
        with open(save,"wb") as pdf: 
            for chunk in r.iter_content(chunk_size=1024): 
                 # writing one chunk at a time to pdf file 
                 if chunk: 
                     pdf.write(chunk)
        print('File downloaded, Check directory')

    
    def checkFile(self):
        pass
    
    
if __name__=="__main__":
    n=New()
    url=str(input('Enter url of file to be downloaded : '))
    saveas=str(input('What name do you want it to be stored as : '))
    n.dw(url,saveas)