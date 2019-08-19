#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 8:31 PM
# @Author  : Slade
# @File    : LeetCode47permutations-ii.py
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        length = len(nums)

        def traceback(idx, tmp, used):
            if idx == len(nums):
                if tmp not in ans:
                    ans.append(tmp)
                return
            for i in range(length):
                if i not in used:
                    traceback(idx + 1, tmp + [nums[i]], used + [i])

        traceback(0, [], [])
        return ans