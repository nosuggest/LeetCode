#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 4:40 PM
# @Author  : Slade
# @File    : LeetCode53maximum-subarray.py.py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)