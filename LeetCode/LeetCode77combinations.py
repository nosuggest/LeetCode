#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 9:15 PM
# @Author  : Slade
# @File    : LeetCode77combinations.py
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        candidates = list(range(1, 1 + n))
        l = len(candidates)
        ans = []
        self.dfs(candidates, 0, 0, l, [], ans, k)
        return ans

    def dfs(self, candidates, length, start, size, tmp, ans, k):
        if length == k:
            ans.append(tmp)
            return

        for index in range(start, size):
            self.dfs(candidates, length + 1, index + 1, size, tmp + [candidates[index]], ans, k)
