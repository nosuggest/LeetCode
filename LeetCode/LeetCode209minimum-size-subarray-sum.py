#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 3:38 PM
# @Author  : Slade
# @File    : LeetCode209minimum-size-subarray-sum.py

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if s > sum(nums):
            return 0

        length = len(nums)
        start = end = 0
        min_cnt = float("inf")
        while end < length:
            while sum(nums[start:end]) < s and end < length:
                end += 1

            while sum(nums[start:end]) >= s and start < end:
                min_cnt = min(min_cnt, end - start)
                start += 1
        return min_cnt if min_cnt != float("inf") else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
