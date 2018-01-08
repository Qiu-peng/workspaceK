# -*- coding: utf-8 -*-

import base64
from Crypto.Cipher import AES


BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

class Aes:
    key = None
    # mode = None
    encryptor = None

    def __init__(self):
        self.mode = AES.MODE_CBC

    def specifykey(self, key):
        self.key = key
        self.encryptor = AES.new(self.key)

    def encrypt(self, plaintext):
        return base64.b64encode(self.encryptor.encrypt(pad(plaintext)))

    def decrypt(self, ciphertext):
        un64_text = base64.b64decode(ciphertext)
        return unpad(self.encryptor.decrypt(un64_text).decode("utf-8"))
