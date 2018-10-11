#!/usr/bin/env python

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom

BLOCKLEN=16
def blocks(data):
	split = [hexa(data[i:i+BLOCKLEN]) for i in range (0,len(data),BLOCKLEN)]
	return ' '.join(split)

k=urandom(16)
print "k=%s" % hexa(k)

# create an instance of AES-128 to encrypt and decrypt
cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
aes_encrypt = cipher.encryptor()

# set plaintext block p to the all-zero string
p='\x00'*BLOCKLEN*2

# encrypt plaintext p to ciphertext c
c=aes_encrypt.update(p) + aes_encrypt.finalize()
print "enc(%s)=%s" % (blocks(p), blocks(c))
