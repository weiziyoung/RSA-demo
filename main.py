# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 5:16 AM
# @Author  : weiziyang
# @FileName: main.py
# @Software: PyCharm


from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)
private_pem = rsa.exportKey()
public_pem = rsa.publickey().exportKey()
pass