#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 3:16 PM
# @Author  : Slade
# @File    : LeetCode283move-zeroes.py
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cur] = nums[i]
                cur += 1
        nums[cur :] = [0]*len(nums[cur :])
        return nums