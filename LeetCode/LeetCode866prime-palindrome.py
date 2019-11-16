#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode866prime-palindrome.py
@Author: sladesha
@Date  : 2019/11/16 13:11
@Desc  : 
'''

import math


class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """

        def is_prime(N):
            if N == 1:
                return False
            for i in range(2, int(math.sqrt(N)) + 1):
                if N % i == 0:
                    return False
            return True

        def is_palindrome(N):
            return str(N) == str(N)[::-1]

        while True:
            # 数学规律1：除 11 外的偶数位回文数，都能被 11 整除
            if len(str(N)) % 2 == 0 and N > 11:
                # 比如1001，直接从10001开始
                N = 10 ** len(str(N)) + 1
                continue
            if is_palindrome(N) and is_prime(N):
                return N
            N += 1
