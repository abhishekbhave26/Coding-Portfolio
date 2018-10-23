# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:06:55 2018

@author: abhis
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS

filename = "one.txt"
key = DSA.generate(3072)

#h = SHA256.new(message)
sha256_hash = SHA256.new()

with open(filename,"rb") as f:

    # Read and update hash string value in blocks of 512 bytes

    for byte_block in iter(lambda: f.read(1024),b""):

        sha256_hash.update(byte_block)
    
    print(sha256_hash.hexdigest())
    #end = time.time()
    #print(end - start)

#sha256_hash = sha256_hash.hexdigest()
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(sha256_hash)

verifier = DSS.new(key, 'fips-186-3')
try:
     verifier.verify(sha256_hash, signature)
     print("The message is authentic.")
except ValueError:
     print ("The message is not authentic.")


    