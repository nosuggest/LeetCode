#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 8:47 AM
# @Author  : Slade
# @File    : LeetCode 491 increasing-subsequences.py
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = set()
        self.get_ans(nums, ())
        return list(self.ans)

    def get_ans(self, nums, tmp):
        if len(tmp) > 1 and tmp not in self.ans:
            self.ans.add(tmp)

        for i in range(len(nums)):
            if len(tmp) == 0:
                self.get_ans(nums[(i + 1):], [nums[i]])
            else:
                if tmp[-1] <= nums[i]:
                    self.get_ans(nums[(i + 1):], tuple(list(tmp) + [nums[i]]))


if __name__ == "__main__":
    s = Solution()
    print(s.findSubsequences([1, 2, 3, 4]))


