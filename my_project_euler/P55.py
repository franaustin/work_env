#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/5
# @Author  : chex
__title__ = ''
__description__ = """
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number
is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will
either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists,
has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty
iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
"""
__description_cn__ = """利克瑞尔数:
我们将47与它的逆转相加，47 + 74 = 121, 可以得到一个回文。
并不是所有数都能这么快产生回文，例如：
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
也就是说349需要三次迭代才能产生一个回文。
虽然还没有被证明，人们认为一些数字永远不会产生回文，例如196。
那些永远不能通过上面的方法（逆转然后相加）产生回文的数字叫做Lychrel数。
因为这些数字的理论本质，同时也为了这道题，我们认为一个数如果不能被证明的不是Lychrel数的话，那么它就是Lychre数。
此外，对于每个一万以下的数字，你还有以下已知条件：
这个数如果不能在50次迭代以内得到一个回文，那么就算用尽现有的所有运算能力也永远不会得到。
10677是第一个需要50次以上迭代得到回文的数，它可以通过53次迭代得到一个28位的回文：4668731596684224866951378664。
令人惊奇的是，有一些回文数本身也是Lychrel数，第一个例子是4994。
10000以下一共有多少个Lychrel数？
注:2007年4月24日措辞略有修改,强调理论的本质利克瑞尔数。
"""
def valid_palindromic(number):
    is_palindromic = False
    num_text = str(number)
    num_len = len(num_text)
    if num_text[:num_len//2] == num_text[-1:-(num_len//2+1):-1]:
        is_palindromic = True
    return is_palindromic

max_number = 10000
results = []  # 349,943,1292,2921,3124,4213,196
for num in xrange(max_number):
    number = num
    is_palindromic = False
    for deep in xrange(50):
        number += int(str(number)[::-1])   # 传递值 n = n + r(n), n = n+r(n) + r(n+r(n))
        is_palindromic = valid_palindromic(number)
        if is_palindromic:
            break
    if not is_palindromic:
        results.append(num)

print len(results)