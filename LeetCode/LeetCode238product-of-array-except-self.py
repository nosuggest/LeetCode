#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode238product-of-array-except-self.py
@Author: sladesha
@Date  : 2019/10/25 22:33
@Desc  : 
'''
from functools import reduce


class Solution(object):
    # 超时
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums = [1] + nums + [1]
        for i in range(1, len(nums) - 1):
            ans.append(reduce(lambda x, y: x * y, nums[:i]) * reduce(lambda x, y: x * y, nums[i + 1:]))
        return ans

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp_val = 1
        tmp = [0]*len(nums)
        for i in range(len(nums)):
            tmp[i] = tmp_val
            tmp_val*=nums[i]
        tmp_val = 1
        for i in range(len(nums)-1,-1,-1):
            tmp[i] = tmp_val*tmp[i]
            tmp_val *= nums[i]
        return tmp

if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
