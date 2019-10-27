#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 3:39 PM
# @Author  : Slade
# @File    : LeetCode96unique-binary-search-trees.py

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        # 只有一个数字的时候，必然为根结点，只有一种结果
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # 左右子树的分别数量的笛卡尔积
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(3))
