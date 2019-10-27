#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 9:06 PM
# @Author  : Slade
# @File    : LeetCode740delete-and-earn.py

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        target = [0] * (max(nums) + 1)
        for num in nums:
            target[num] += num
        d = list(range(len(target)))

        d[0] = target[0]
        d[1] = target[1]

        for i in range(2, len(target)):
            d[i] = max(d[i - 1], d[i - 2] + target[i])
        return d[-1]


