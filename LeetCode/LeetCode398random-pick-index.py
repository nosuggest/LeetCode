#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 11:06 AM
# @Author  : Slade
# @File    : LeetCode398random-pick-index.py.py
from random import randint


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = None
        for i, v in enumerate(self.nums):
            if v == target:
                # k/(k+1)被保留
                if not randint(0, cnt):
                    res = i
                cnt += 1
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
