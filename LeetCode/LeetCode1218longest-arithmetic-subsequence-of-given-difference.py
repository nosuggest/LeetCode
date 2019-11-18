#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode1218longest-arithmetic-subsequence-of-given-difference.py
@Author: sladesha
@Date  : 2019/11/18 22:47
@Desc  : 
'''

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i-difference,0)+1
        return max(hashmap.values())

if __name__ == '__main__':
    print(Solution().longestSubsequence([1,5,7,8,5,3,4,2,1],-2))