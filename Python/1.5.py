from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import base64

def encrypt_blob(blob, public_key):
    rsa_key = RSA.importKey(public_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    
    chunk_size = 200
    offset = 0
    end_loop = False
    encrypted = b""

    while not end_loop:
        
        chunk = blob[offset:offset + chunk_size]
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += b""*(chunk_size - len(chunk))

        #Append the encrypted chunk to the overall encrypted file
        encrypted += rsa_key.encrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    return base64.b64encode(encrypted)

def decrypt_blob(encrypted_blob, private_key):

    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    encrypted_blob = base64.b64decode(encrypted_blob)
    chunk_size = 384
    offset = 0
    decrypted = b""

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    return decrypted

def calcPerByte(filesize,x):
    x*=1000000
    print("Per byte time is {} microsecond".format(x/filesize))

print('For 2048 bit')

start=time.time()
#Generate a public/ private key pair using 2048 bits key length (512 bytes)
new_key = RSA.generate(2048, e=65537)
end = time.time()
x=end-start
print(x)
calcPerByte(1048576,x)
#The private key in PEM format
private_key = new_key.exportKey("PEM")

#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

print(private_key)
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print(public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

#Use the public key for encryption
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

#Our candidate file to be encrypted
fd = open("one.txt", "rb")
unencrypted_blob = fd.read()
fd.close()

start = time.time()
encrypted_blob = encrypt_blob(unencrypted_blob, public_key)
end = time.time()
x=end-start
print(x)
calcPerByte(1048576,x)

#Write the encrypted contents to a file
fd = open("encrypted_one.txt", "wb")
fd.write(encrypted_blob)
fd.close()


#Use the private key for decryption
fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

#Our candidate file to be decrypted
fd = open("encrypted_one.txt", "rb")
encrypted_blob = fd.read()
fd.close()

#Write the decrypted contents to a file
fd = open("decrypted_one.txt", "wb")
start=time.time()
fd.write(decrypt_blob(encrypted_blob, private_key))
end = time.time()
x=end-start
print(x)
calcPerByte(1048576,x)
fd.close()
