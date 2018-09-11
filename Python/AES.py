# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:57:46 2018

@author: abhis
"""


from Crypto.Cipher import AES
import time
import random, string
start = time.time()


#key='CE893D9F1BE38DC607E1CFEB71E2B0DE'



for i in range(1001):
    #encryption
    message= ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    key=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    print('Message is {} for {} time'.format(message,i))
    obj = AES.new(key, AES.MODE_ECB)
    ciphertext = obj.encrypt(message)
    print('Ciphertext is {}'.format(ciphertext))

    #decryption
    obj2 = AES.new(key, AES.MODE_ECB)
    decrypt=obj2.decrypt(ciphertext)
    new=str(decrypt, 'utf-8')
    print('Decrypted Message is {}'.format(new))

end = time.time()
print(end - start)



# key generator https://asecuritysite.com/encryption/keygen
#code https://github.com/dlitz/pycrypto/blob/master/README