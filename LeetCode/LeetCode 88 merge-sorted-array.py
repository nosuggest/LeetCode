#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode 88 merge-sorted-array.py
@Author: sladesha
@Date  : 2019/8/13 21:45
@Desc  : 
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        nums1.sort()