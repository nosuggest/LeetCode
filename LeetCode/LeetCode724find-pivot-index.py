#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode724find-pivot-index.py
@Author: sladesha
@Date  : 2020/1/1 20:41
@Desc  : 
'''


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        s = sum(nums)
        tmp = 0
        for i in range(0, len(nums)):
            tmp += nums[i - 1] if i >= 1 else 0
            if tmp == s - tmp - nums[i]:
                return i

        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex([-1, -1, -1, 0, 1, 1]))
