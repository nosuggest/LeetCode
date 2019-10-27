#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode63unique-paths-ii.py
@Author: sladesha
@Date  : 2019/8/13 21:31
@Desc  : 
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
        print(obstacleGrid)
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    s = Solution()
    mat = [[0,1]]
    print(s.uniquePathsWithObstacles(mat))
