#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode494target-sum.py
@Author: sladesha
@Date  : 2019/9/20 23:21
@Desc  : 
'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        numsSum = sum(nums)
        if numsSum < S or (S + numsSum) % 2 != 0:
            return 0

        P = (S + numsSum) // 2
        # 合成0只有什么都不干一种方式
        dp = [1] + [0 for i in range(P)]
        for num in nums:
            # 目标是把P的背包容量装满
            i = P
            while i >= num:
                # 类似爬楼梯、临近数问题，组成i有两种可能dp[i]或者dp[i-num](即i-num的可能数+num)
                dp[i] = dp[i] + dp[i - num]
                i -= 1
        return dp[P]

if __name__ == '__main__':
    s = Solution()
    print (s.findTargetSumWays([1,1,1,1,1],3))