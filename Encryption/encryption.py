# -*- coding: utf-8 -*-
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
    
    
if __name__ == "__main__":
    given_str = "hello worldrtherthetrh546uy56u56$U%^U%^U^%&U$^&I^&IYUTR"
    enc_str = encode("alantai", given_str)
    dec_str = decode("alantai", enc_str)
    
    print enc_str
    print dec_str
    print u"哈哈"