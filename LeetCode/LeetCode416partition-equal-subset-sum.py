#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 8:39 AM
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
 

示例 2:

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

        dp = [[0 for i in range(1, cutOff + 1)] for j in nums]

        row = len(dp)
        col = len(dp[0])

        # 初始化
        for i in range(0, col):
            if i + 1 == nums[0]:
                dp[0][i] = 1

        for i in range(1, row):
            for j in range(0, col):
                # 当前值
                if j + 1 == nums[i]:
                    dp[i][j] = 1
                # 上次结果
                if dp[i - 1][j]:
                    dp[i][j] = 1
                # 上次结果+当前值
                if j + 1 > nums[i] and dp[i - 1][j - nums[i]]:
                    dp[i][j] = 1
            # 不加以下代码会超时，因为只要有一个行满足条件，没有必要再试其他的，剩下的各个元素都不取即可
            if dp[i][-1]:
                return True
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
