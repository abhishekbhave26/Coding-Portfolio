# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:40:00 2019

@author: abhis
"""

import time
import webbrowser
import random

while(True):
    sites=random.choice(['google.com','youtube.com','facebook.com','freecodecamp.com','linkedin.com'])
    visit='http://{}'.format(sites)
    webbrowser.open(visit)
    seconds=random.randrange(5,15)
    time.sleep(seconds)
    