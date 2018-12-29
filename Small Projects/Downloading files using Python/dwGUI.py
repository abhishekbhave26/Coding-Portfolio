# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:46:42 2018

@author: abhis
"""

import tkinter
from tkinter import *
import download as d
import downloadLarge as dl
import downloadVideo as dv
#tkinter._test()


class GUI():
    
    #d.NewClass.dw(d,'https://media.licdn.com/dms/image/C5603AQE5O_37obn3Ew/profile-displayphoto-shrink_200_200/0?e=1551312000&v=beta&t=sAKZ69APiPt2vQMZL8MYKI-jYliyxvYB6uDNYUg7VNg','new.jpg')

    def createGUI(self):
        
        root=Tk()
        
        # Set the background colour of GUI window  
        root.configure(background = 'light blue')  
        
        # Set the configuration of GUI window (WidthxHeight) 
        root.geometry("550x350") 
        
        menu = Menu(root) 
        root.config(menu=menu) 
        filemenu = Menu(menu) 
        menu.add_cascade(label='File', menu=filemenu) 
        filemenu.add_command(label='New') 
        filemenu.add_command(label='Open...') 
        filemenu.add_separator() 
        filemenu.add_command(label='Exit', command=root.quit) 
        helpmenu = Menu(menu) 
        menu.add_cascade(label='Help', menu=helpmenu) 
        helpmenu.add_command(label='About') 
        
        T = Text(root, height=3, width=30,highlightcolor='black',font=40) 
        T.pack() 
        T.insert(END, 'Welcome to File Downloader') 
        
        frame = Frame(root) 
        frame.pack()
        
       
        
        bottomframe = Frame(root) 
        bottomframe.pack( side = BOTTOM ) 
        redbutton = Button(frame, text = 'Image File Download \n\n Enter image url below', width=25, height=10,command=d.NewClass.dw(d,'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png','new1.png')) 
        redbutton.pack( side = LEFT) 
        greenbutton = Button(frame, text = 'Download Large File \n\n Enter file url below',width=25, height=10,) 
        greenbutton.pack( side = LEFT ) 
        bluebutton = Button(frame, text ='Scrape URL for videos  \n\n Enter url below ', width=25, height=10)
        bluebutton.pack( side = LEFT ) 
        
        
        
        

        
        blackbutton = Button(bottomframe, text ='Exit', command=root.destroy,width=15, height=10) 
        blackbutton.pack( side = BOTTOM) 
        root.mainloop() 
        
    
        
        
        
if __name__=="__main__":
    n=GUI()
    #n.makeGUI()
    n.createGUI()