#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 2:55 PM
# @Author  : Slade
# @File    : LeetCode221maximal-square.py.py
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxArea = 0
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        dp = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                maxArea = 1
            else:
                dp[i][0] = 0

        for i in range(col):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                maxArea = 1
            else:
                dp[0][i] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    if dp[i][j] > maxArea:
                        maxArea = dp[i][j]
                else:
                    dp[i][j] = 0
        return maxArea ** 2


if __name__ == '__main__':
    mat = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
    s = Solution()
    print(s.maximalSquare(mat))
