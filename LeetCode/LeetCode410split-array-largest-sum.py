#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 10:19 AM
# @Author  : Slade
# @File    : LeetCode410split-array-largest-sum.py
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        if len(nums) == m:
            return left

        while (left < right):
            # 每个子数组的最大和应该在max(原数组)和sum(原数组)之间
            mid = (left + right) // 2
            tmpSum = 0
            cnt = 1
            for num in nums:
                tmpSum += num
                if tmpSum > mid:
                    # 这边新起的时候要考虑把第一个值带进来
                    tmpSum = num
                    cnt += 1
            # 二分
            if cnt > m:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))
