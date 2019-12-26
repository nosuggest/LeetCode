#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 11:01 PM
# @Author  : Slade
# @File    : LeetCode485max-consecutive-ones.py

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(lambda x:len(x),"".join(map(str,nums)).split("0")))