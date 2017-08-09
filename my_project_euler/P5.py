#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/9
# @Author  : chex
__title__ = ''
__description__ = """
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
__description_cn__ = """最小公倍数：
2520是最小的能被1-10整除的数，求能被1-20整除的最小正整数
注：
分解质因素
最小公倍数等于它们所有的质因数的乘积（如果有几个质因数相同，则比较两数中哪个数有该质因数的个数较多，乘较多的次数）
"""


def get_prime_factors(num):
    is_prime = True
    for a in xrange(2, num):
        if num % a == 0:
            is_prime = False
    return is_prime


all_prime_factors = []
for n in xrange(2, 20 + 1):
    if get_prime_factors(n):
        all_prime_factors.append(n)


def get_multiple_root(prime, number):
    count = 0
    while number // prime > 0:
        number = number // prime
        count += 1
    return count


result = 1
for p in all_prime_factors:
    result *= p ** get_multiple_root(p, 20)

print result

# 232792560
