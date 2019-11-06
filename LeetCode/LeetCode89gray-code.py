#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 9:25 PM
# @Author  : Slade
# @File    : LeetCode89gray-code.py

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        dp = ["0", "1"]
        for i in range(n - 1):
            dp = ["0" + i for i in dp] + ["1" + i for i in dp[::-1]]
        return map(lambda x: int(x, base=2), dp)


if __name__ == '__main__':
    print(Solution().grayCode(3))
