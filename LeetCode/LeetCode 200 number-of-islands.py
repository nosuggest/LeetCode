#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode 200 number-of-islands.py
@Author: sladesha
@Date  : 2019/8/19 22:40
@Desc  : 
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        col = len(grid)
        row = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[j][i]=0
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                i_move = i + x
                j_move = j + y
                if 0 <= i_move < row and 0 <= j_move < col and grid[j_move][i_move] == "1":
                    dfs(i_move, j_move)
            print(grid)


        for i in range(col):
            for j in range(row):
                if grid[i][j] == "1":
                    dfs(j, i)
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    mat = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(s.numIslands(mat))
