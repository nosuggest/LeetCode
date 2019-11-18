#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode594longest-harmonious-subsequence.py
@Author: sladesha
@Date  : 2019/11/18 22:37
@Desc  : 
'''


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1

        tmp = 0
        for k,v in hashmap.items():
            match = max(hashmap.get(k-1,0),hashmap.get(k+1,0))
            if not match:
                continue
            tmp = max(tmp,hashmap.get(k)+match)
        return tmp