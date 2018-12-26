# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 17:57:24 2018

@author: abhis
"""

from selenium import webdriver 

from selenium.webdriver.support.ui import WebDriverWait 

from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.by import By 

import time 

  
# Replace below path with the absolute path 
# to chromedriver in your computer 

driver = webdriver.Chrome('C:/Users/abhis/Desktop/All repositories/Coding-Portfolio/Python/chromedriver.exe') 
driver.get("https://web.whatsapp.com/") 

wait = WebDriverWait(driver, 600)
target = '"Friend\'s Name"'

  
# Replace the below string with your own message 

string = "Message sent using Python!!!"

  

x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located(( 

    By.XPATH, x_arg))) 
group_title.click() 

inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

input_box = wait.until(EC.presence_of_element_located(( 

    By.XPATH, inp_xpath))) 

for i in range(100): 

    input_box.send_keys(string + Keys.ENTER) 

    time.sleep(1) 