#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 5:41 PM
# @Author  : Slade
# @File    : LeetCode152maximum-product-subarray.py
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = nums[0]
        MIN = nums[0]
        dp = [0] * len(nums)
        dp[0] = max(MAX, MIN)
        for i in range(1, len(nums)):
            if nums[i] < 0:
                MAX, MIN = MIN, MAX
            MAX = max(nums[i], nums[i] * MAX)
            MIN = min(nums[i], nums[i] * MIN)
            dp[i] = max(MAX, MIN)
        return max(dp)

