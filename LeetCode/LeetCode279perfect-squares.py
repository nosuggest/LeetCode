#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 9:56 AM
# @Author  : Slade
# @File    : LeetCode279perfect-squares.py
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while i - j ** 2 >= 0:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    for i in range(3006):
        print({"i为{},对应的值为{}".format(i, s.numSquares(i))})
