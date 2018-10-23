# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 20:22:45 2018

@author: abhis
"""
import time
import os, struct
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'

    c = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CTR, counter=lambda:c)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(c)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))



def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
   
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        c = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CTR, counter=lambda:c)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)



def calcPerByte(filesize,x):
    x*=1000000
    print("Per byte time is {} microsecond".format(x/filesize))




print('For 128 bit \n')



key = os.urandom(16)
print('Key generated randomly ')


start = time.time()
encrypt_file(key,'one.txt')
end = time.time()
print('Encryption  time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)

start = time.time()
decrypt_file(key,'one.txt.enc','dec.txt')
end = time.time()
print('Decryption time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)
print('\n')


key = os.urandom(16)
print('Key generated randomly ')


start = time.time()
encrypt_file(key,'1.pdf')
end = time.time()
print('Encryption  time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)

start = time.time()
decrypt_file(key,'1.pdf.enc','out.pdf')
end = time.time()
print('Decryption  time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)
print('\n')

print('For 256 bit \n')
key = os.urandom(32)
print('Key generated randomly ')


start = time.time()
encrypt_file(key,'one.txt')
end = time.time()
print('Encryption  time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)

start = time.time()
decrypt_file(key,'one.txt.enc','dec.txt')
end = time.time()
print('Decryption time 1kb')
x=end-start
print(x)
calcPerByte(1024,x)
print('\n')


key = os.urandom(32)
print('Key generated randomly ')


start = time.time()
encrypt_file(key,'1.pdf')
end = time.time()
print('Encryption  time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)

start = time.time()
decrypt_file(key,'1.pdf.enc','out.pdf')
end = time.time()
print('Decryption  time 1Mb')
x=end-start
print(x)
calcPerByte(1048576,x)