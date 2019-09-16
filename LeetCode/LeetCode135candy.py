#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode135candy.py
@Author: sladesha
@Date  : 2019/9/12 21:59
@Desc  : 
'''


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        nums = ratings

        rnums = [-float("inf")] + nums[::-1]
        nums = [-float("inf")] + nums

        length = len(nums)
        total = []
        rtotal = []
        tmp = 0
        rtmp = 0
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                tmp += 1
                total.append(tmp)
            else:
                tmp = 1
                total.append(tmp)
        for i in range(1, length):
            if rnums[i] > rnums[i - 1]:
                rtmp += 1
                rtotal.append(rtmp)
            else:
                rtmp = 1
                rtotal.append(rtmp)
        return sum(map(lambda x: max(x), zip(total, rtotal[::-1])))