# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:57:16 2018

@author: abhis
"""

import hashlib
import time

def file256(filename):
    
    with open(filename,"rb") as f:

        bytes = f.read() # read entire file as bytes

        readable_hash = hashlib.sha256(bytes).hexdigest();

        print(readable_hash)
        

def file512(filename):
    
    with open(filename,"rb") as f:

        bytes = f.read() # read entire file as bytes

        readable_hash = hashlib.sha512(bytes).hexdigest();

        print(readable_hash)
        

def file3_256(filename):
    
    with open(filename,"rb") as f:
        
        bytes=f.read()
        
        hash=hashlib.sha3_256(bytes).hexdigest();
        
        print(hash)
    
def calcPerByte(filesize,x):
    x*=1000000
    print("Per byte time is {} microsecond".format(x/filesize))
        
        
print('For SHA-256 \n')
start = time.time()
file256('new.txt')
end = time.time()
print('Hash time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)

start = time.time()
file256('new1.txt')
end = time.time()
print('Hash time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)
print('\n')


print('For SHA-512 \n')
start = time.time()
file512('one.txt')
end = time.time()
print('Hash time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)

start = time.time()
file512('1.pdf')
end = time.time()
print('Hash time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)
print('\n')


print('For SHA3-256 \n')
start = time.time()
file3_256('one.txt')
end = time.time()
print('Hash time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)

start = time.time()
file3_256('1.pdf')
end = time.time()
print('Hash time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)

