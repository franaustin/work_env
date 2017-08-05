#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/5
# @Author  : chex
__title__ = ''
__description__ = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000."""
__description_cn__ = """"如果我们列出所有小于10的自然数中3或者5的倍数，我们可以得到3、5、6、9，他们的和是23，
计算所有小于1000的自然数中，3或5的倍数的和。"""
max_number = 1000
result = 0
for num in xrange(max_number):
    if num % 3 == 0 or num % 5 == 0 :
        result += num
print result
# 233168
