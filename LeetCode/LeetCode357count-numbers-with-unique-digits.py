#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:32 AM
# @Author  : Slade
# @File    : LeetCode357count-numbers-with-unique-digits.py

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        def fact(n):
            tmp = 9
            for i in range(1, min(n, 10)):
                tmp = tmp * (9 - i + 1)
            return tmp

        dp = [1] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + fact(i)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(3))
