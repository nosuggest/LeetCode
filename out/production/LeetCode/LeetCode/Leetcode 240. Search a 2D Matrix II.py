#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 2:45 PM
# @Author  : Slade
# @File    : 搜索二维矩阵 II.py
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(matrix)

        if not i:
            return False
        j = len(matrix[0])
        if not j:
            return False
        k= 0
        while k <i:
            for s in range(j):
                if matrix[k][s]==target:
                    return True
            k+=1
        return False

    def searchMatrix1(self, matrix, target):
        return any(target in row for row in matrix)


if __name__ == "__main__":
    obj = Solution()
    print(obj.searchMatrix([], 30))