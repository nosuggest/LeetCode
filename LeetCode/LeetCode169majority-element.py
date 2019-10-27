#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 3:34 PM
# @Author  : Slade
# @File    : LeetCode169majority-element.py
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if cnt == 0:
                ans = num

            if ans == num:
                cnt += 1
            else:
                cnt -= 1
        return ans