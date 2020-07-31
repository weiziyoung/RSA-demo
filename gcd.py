# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 11:27 AM
# @Author  : weiziyang
# @FileName: gcd.py
# @Software: PyCharm


def ext_gcd(a, b):
    if b == 0:
        x1 = 1
        y1 = 0
        x = x1
        y = y1
        r = a
        return r, x, y
    else:
        r, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - a // b * y1
        return r, x, y
