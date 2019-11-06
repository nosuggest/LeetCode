#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 12:04 AM
# @Author  : Slade
# @File    : LeetCode213house-robber-ii.py

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        if len(nums) == 3:
            return max(nums[1], max(nums[0], nums[2]))

        dp0 = [0] * len(nums)
        dp1 = [0] * len(nums)
        dp0[0] = nums[0]
        dp0[1] = max(nums[:2])
        dp1[1] = nums[1]
        for i in range(2, len(nums)):
            dp0[i] = max(dp0[i - 1], dp0[i - 2] + nums[i])
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        return max(max(dp0[-2], dp0[-3]), max(dp1[-2], dp1[-3] + nums[-1]))


if __name__ == '__main__':
    print(Solution().rob([2, 7, 9, 3, 1]))
