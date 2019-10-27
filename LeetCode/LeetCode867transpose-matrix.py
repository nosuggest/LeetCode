#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 11:53 AM
# @Author  : Slade
# @File    : LeetCode867transpose-matrix.py

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])

        ret = [[0 for i in range(row)] for j in range(col)]

        for i in range(row):
            for j in range(col):
                ret[j][i] = A[i][j]

        return ret


if __name__ == '__main__':
    print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
