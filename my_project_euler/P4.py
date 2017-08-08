#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/8
# @Author  : chex
__title__ = ''
__description__ = """
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
__description_cn__ = """回文是指从左至右跟从右至左读都是一样的数字，最大的两个两位数乘积产生的回文是9009 = 91 × 99.
找出由两个三位数乘积构成的最大的回文"""
palindrome_3d_max = 0
x = 0
y = 0
for a in xrange(1000-1,100-1,-1):
    for b in xrange(1000-1,100-1,-1):
        num = a * b
        if str(num) == str(num)[::-1]:
            if palindrome_3d_max < num:
                palindrome_3d_max = num
                x, y = a, b
print "%s = %s * %s" %(palindrome_3d_max, x, y)
# 906609 = 993 * 913
