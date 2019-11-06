#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 7:28 PM
# @Author  : Slade
# @File    : LeetCode216combination-sum-iii.py
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = list(range(1, 10))
        ans = []
        self.dfs(candidates, 0, len(candidates), n, [], ans, k, 0)
        return ans

    def dfs(self, candidates, start, size, residue, tmp, ans, k, length):
        if len(tmp) == k and residue == 0:
            ans.append(tmp[:])
            return

        for index in range(start, size):
            if len(tmp) == k or residue < candidates[index]:
                break

            self.dfs(candidates, index + 1, size, residue - candidates[index], tmp + [candidates[index]], ans, k,
                     length + 1)
