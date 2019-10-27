#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 8:14 PM
# @Author  : Slade
# @File    : LeetCode704binary-search.py
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        first = 0
        last = len(nums)
        while first < last:
            mid = first + (last-first)//2
            if nums[mid]<target:
                first = mid + 1
            else:
                last = mid
        return first