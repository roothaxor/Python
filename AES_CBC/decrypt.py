#!/usr/bin/env python
import base64, hashlib
from Crypto import Random
from Crypto.Cipher import AES
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

def decrypt():
    filename = raw_input('Input file name: ')
	cipher = AESCipher('thisiscipheryoo')
	file = open(filename,'r')
	file = file.read()
	decrypted = cipher.decrypt(file)
	fil = open(filename, 'w')
	fil.write(decrypted)
	fil.close()
	#print encrypted