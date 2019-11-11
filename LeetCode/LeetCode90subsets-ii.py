#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 4:43 PM
# @Author  : Slade
# @File    : LeetCode90subsets-ii.py
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        for num in nums:
            for item in ans[:]:
                if item + [num] not in ans:
                    ans.append(item + [num])
        return ans


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        res = []

        def helper(idx, tmp):
            res.append(tmp)
            for i in range(idx, length):
                if i > idx and nums[i - 1] == nums[i]:
                    continue
                helper(i + 1, tmp + nums[i])

        helper(0, [])
        return res
