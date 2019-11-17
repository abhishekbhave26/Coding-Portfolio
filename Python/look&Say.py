# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:56:49 2019

@author: abhis
"""

def look_and_say(num):  
      result = '1'
      for i in range(1, num):
        new_result = ''
        chr = result[0]
        count = 0
        for c in result:
          if chr == c:
            count += 1
          else:
            new_result += str(count) + chr
            count = 1
            chr = c
    
        result = new_result + str(count) + chr

      return result
  
print(look_and_say(6))
