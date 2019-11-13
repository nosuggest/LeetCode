#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 9:53 AM
# @Author  : Slade
# @File    : LeetCode1071greatest-common-divisor-of-strings.py

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # 需要表示为N*最大公因子的形式
        if str1+str2!=str2+str1:
            return ""
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)
        return str1[:gcd(len(str1),len(str2))]

if __name__ == '__main__':
    print(Solution().gcdOfStrings("LEET","CODE"))