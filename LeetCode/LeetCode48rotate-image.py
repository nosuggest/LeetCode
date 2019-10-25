#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode48rotate-image.py
@Author: sladesha
@Date  : 2019/10/25 22:30
@Desc  : 
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        def transfer(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        ans = []
        mat = transfer(matrix)
        for i in mat:
            ans.append(i.reverse())
        return ans
