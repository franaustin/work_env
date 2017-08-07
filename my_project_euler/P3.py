#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/7
# @Author  : chex
__title__ = ''
__description__ = """
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
__description_cn__ = """
13195的质因数是5,7,13和29.
求600851475143的最大质因数
注:
质因数（素因数或质因子）在数论里是指能整除给定正整数的质数。除了1以外，两个没有其他共同质因子的正整数称为互质。
因为1没有质因子，1与任何正整数（包括1本身）都是互质。正整数的因数分解可将正整数表示为一连串的质因子相乘，质因子如重复可以
指数表示。根据算术基本定理，任何正整数皆有独一无二的质因子分解式。只有一个质因子的正整数为质数
"""
num = 600851475143
factor = 2
result = 1
while num > 2 :
    if num % factor == 0:
        result = factor
        num = num / factor
        while num % factor==0:
            num = num / factor
    factor += 1
print result