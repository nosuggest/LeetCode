#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 5:28 PM
# @Author  : Slade
# @File    : LeetCode 300 longest-increasing-subsequence.py

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(last_value, idx):
            if idx == len(nums):
                # 终止条件：最后一个值后无可追加的子序列，返回0
                return 0
            # 如果last_value < nums[idx]可以选择接受这个num[idx]，并进行以该值做last_Value的下个递归进程
            take = 0
            if last_value < nums[idx]:
                take = 1 + helper(nums[idx], idx + 1)
            # 我也可以选择不接受这个num[idx]或者压根就比last_value要小，我就捏着上一个递增序列的最后一个值去找下个位置
            no_take = helper(last_value, idx + 1)

            # 比较接受与不接受的情况下，哪个更大
            return max(take, no_take)

        return helper(-float("inf"), 0)
