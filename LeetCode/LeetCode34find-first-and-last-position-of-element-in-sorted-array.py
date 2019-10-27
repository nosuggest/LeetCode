#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 8:48 PM
# @Author  : Slade
# @File    : LeetCode34find-first-and-last-position-of-element-in-sorted-array.py

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            # 找左边界的时候是向下整除
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        start = left

        left = 0
        right = len(nums) - 1
        while left < right:
            # 找右边界的时候是需要想上整除
            mid = (left + right + 1) >> 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        end = right
        if start <= end and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]


if __name__ == '__main__':
    print(Solution().searchRange([1], 0))
