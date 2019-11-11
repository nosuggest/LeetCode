#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 2:22 PM
# @Author  : Slade
# @File    : LeetCode416partition-equal-subset-sum.py
'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false

解释: 数组不能分割成两个元素和相等的子集.
'''


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSum = sum(nums)
        if numsSum % 2:
            return False
        else:
            cutOff = int(numsSum / 2)

        dp = [[0 for i in range(cutOff + 1)] for j in nums]

        # 初始化,第一个值是否可以达到cutoff
        for i in range(cutOff + 1):
            if i == nums[0]:
                dp[0][i] = True

        for i in range(1, len(nums)):
            for j in range(cutOff + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i] and dp[i - 1][j - nums[i]]:
                    dp[i][j] = True

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
