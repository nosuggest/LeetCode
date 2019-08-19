#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 10:06 AM
# @Author  : Slade
# @File    : LeetCode 892 surface-area-of-3d-shapes.py
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid)
        row = len(grid[0])
        upper, left, head = 0, 0, 0

        for i in range(col):
            for j in range(row):
                upper += min(1, grid[i][j])
        upper *= 2

        for i in range(col):
            left += grid[i][0] + grid[i][row - 1]
            for j in range(row - 1):
                left += abs(grid[i][j] - grid[i][j + 1])

        for i in range(row):
            head += grid[0][i] + grid[col - 1][i]
            for j in range(col - 1):
                head += abs(grid[j][i] - grid[j + 1][i])
        return upper + head + left


if __name__ == '__main__':
    s = Solution()
    val = [[1,1,1],[1,0,1],[1,1,1]]
    print(s.surfaceArea(val))
