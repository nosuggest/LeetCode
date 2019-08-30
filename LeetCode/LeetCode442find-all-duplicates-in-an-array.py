#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 10:43 AM
# @Author  : Slade
# @File    : LeetCode442find-all-duplicates-in-an-array.py.py

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for idx in range(len(nums)):
            new_idx = abs(nums[idx]) - 1
            if nums[new_idx] > 0:
                nums[new_idx] *= -1
            else:
                ans.append(new_idx + 1)
        return ans



if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))
