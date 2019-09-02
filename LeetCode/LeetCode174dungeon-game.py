#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 4:18 PM
# @Author  : Slade
# @File    : LeetCode174dungeon-game.py.py
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row = len(dungeon)
        col = len(dungeon[0])
        if not col:
            return 1

        dp = [[0 for i in range(col)] for j in range(row)]
        dp[row - 1][col - 1] = max(0, -dungeon[row - 1][col - 1]) + 1

        for i in range(row - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for j in range(col - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    # mat = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    mat = [[0, -3]]
    print(s.calculateMinimumHP(mat))