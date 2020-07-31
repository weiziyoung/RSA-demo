# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 2:33 PM
# @Author  : weiziyang
# @FileName: rsa.py
# @Software: PyCharm
from generate_prime import PrimeGenerator, montgomery
from gcd import ext_gcd


class RSA(object):
    def __init__(self,):
        while True:
            self.p, self.q = PrimeGenerator().generate_pq()
            self.n = self.p * self.q

            self.euler = (self.p - 1) * (self.q - 1)
            self.d_num = 65537
            self.e_num = ext_gcd(self.d_num, self.euler)[1]
            if self.e_num > 0:
                break

        self.pub_key = (self.n, self.e_num)
        self.private_key = (self.n, self.d_num)

    def encrypt(self, text):
        text_num = int(''.join([str(ord(each)).zfill(5) for each in text]))
        ciphered_unicode = montgomery(text_num, self.d_num, self.n)
        return ciphered_unicode

    def decrypt(self, cipher):
        ori_unicode = str(montgomery(cipher, self.e_num, self.n))
        ori_string = ''
        right_cursor = len(ori_unicode)
        while right_cursor > 0:
            start_cursor = (right_cursor - 5) if (right_cursor-5) > 0 else 0
            char_cipher = ori_unicode[start_cursor:right_cursor]
            ori_string += chr(int(char_cipher))
            right_cursor -= 5
        return ''.join(list(reversed(ori_string)))


if __name__ == "__main__":
    rsa = RSA()
    text = '你爸爸是我'
    ciphered_code = rsa.encrypt(text)
    ori_text = rsa.decrypt(ciphered_code)
    print(ori_text)
    assert ori_text == text
