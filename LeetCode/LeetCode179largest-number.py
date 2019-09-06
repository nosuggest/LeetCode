#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 7:26 PM
# @Author  : Slade
# @File    : LeetCode179largest-number.py
from functools import cmp_to_key


class Solution(object):
    def sort(self, s1, s2):
        if s1 + s2 > s2 + s1:
            return 1
        elif s1 + s2 < s2 + s1:
            return -1
        else:
            return 0

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        if len(set(nums)) == 1 and 0 in nums:
            return "0"
        return ''.join(sorted(map(str, nums), key=cmp_to_key(self.sort), reverse=True))


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([0, 0]))
