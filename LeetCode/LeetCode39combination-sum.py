#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 6:51 PM
# @Author  : Slade
# @File    : LeetCode39combination-sum.py
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        ans = []
        self.dfs(candidates, 0, len(candidates), target, [], ans)
        return ans

    def dfs(self, candidates, start, size, residue, tmp, ans):
        if residue == 0:
            ans.append(tmp[:])
            return

        for index in range(start, size):
            if candidates[index] > residue:
                continue

            # 核心，因为不想重复，所以start处不能重复，每次都从当前位置往后去搜
            self.dfs(candidates, index, size, residue - candidates[index], tmp + [candidates[index]], ans)
