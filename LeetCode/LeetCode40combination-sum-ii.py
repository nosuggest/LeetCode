#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 6:20 PM
# @Author  : Slade
# @File    : LeetCode40combination-sum-ii.py
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not len(candidates):
            return []
        candidates.sort()
        ans = []
        self.dfs(candidates, len(candidates), 0, [], target, ans)
        return ans

    def dfs(self, candidates, size, start, tmp, residue, ans):
        if not residue:
            ans.append(tmp[:])
            return

        for index in range(start, size):
            if candidates[index] > residue:
                break

            # 去重candidates[index - 1] == candidates[index]
            # index > start保证同一次dfs内连续两个值不被丢弃，不同的两次dfs中会去重
            if index > start and candidates[index - 1] == candidates[index]:
                continue

            # tmp.append(candidates[index])
            # 从下一个位置index+1开始走
            self.dfs(candidates, size, index + 1, tmp + candidates[index], residue - candidates[index], ans)

            # # 跳过该值
            # tmp.pop()
