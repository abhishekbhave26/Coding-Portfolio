# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:03:50 2019

@author: abhis
"""
#leetcode 535


import random
import string
dic={}

class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        lettersAndDigits = string.ascii_letters + string.digits    
        x=''.join(random.choice(lettersAndDigits) for i in range(0,6))
        dic[x]=longUrl
        return x
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if(shortUrl in dic):
            return dic[shortUrl]
        else:
            return None        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
     
        
        

import random
dic={}
dic2={}
class Codec2:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        dic[longUrl]=str(random.randint(1,100))
        dic2["https://tinyurl.com/"+dic[longUrl]]=longUrl
        return "https://tinyurl.com/"+dic[longUrl]
        
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return dic2[shortUrl]