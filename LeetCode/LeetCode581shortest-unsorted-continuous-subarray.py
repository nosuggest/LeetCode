#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 11:00 AM
# @Author  : Slade
# @File    : LeetCode581shortest-unsorted-continuous-subarray.py
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [i for i, (a, b) in enumerate(zip(sorted(nums), nums)) if a != b]
        return max(d) - min(d) + 1 if len(d) else 0