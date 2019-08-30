#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 9:14 AM
# @Author  : Slade
# @File    : test13.py
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            # nums中num对应的idx下的nums中的数强制为负数
            nums[abs(nums[idx]) - 1] = -abs(nums[abs(nums[idx]) - 1])

        ans = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                ans.append(idx + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
