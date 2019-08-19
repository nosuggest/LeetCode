#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 7:48 PM
# @Author  : Slade
# @File    : LeetCode829consecutive-numbers-sum.py
import math


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in range(1, math.ceil(math.sqrt(2 * N))):
            '''a*(a+i)=2N,所以a要小于sqrt(2N)'''
            c, m = divmod(2 * N, i)
            if m == 0:
                if (c % 2 + i % 2) == 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.consecutiveNumbersSum(15))
