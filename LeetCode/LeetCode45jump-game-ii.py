#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 10:29 AM
# @Author  : Slade
# @File    : LeetCode45jump-game-ii.py

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [float("inf")] * length
        dp[0] = 0
        for i in range(0, length):
            for j in range(1, nums[i] + 1):
                if i + j >= length:
                    break
                offset = i + j
                dp[offset] = min(dp[i] + 1, dp[offset])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
