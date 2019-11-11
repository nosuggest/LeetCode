#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 5:25 PM
# @Author  : Slade
# @File    : LeetCode698Partition-to-K-Equal-Sum-Subsets.py

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s%k!=0:
            return False
        else:
            target = int(s/k)
        mask = [False]*len(nums)
        length = len(nums)
        def search(nums,mask,target,tmp_sum,idx,start):
            if idx==1:
                return True
            if tmp_sum==target:
                return search(nums,mask,target,0,idx-1,0)
            for i in range(start,len(nums)):
                if mask[i]:
                    continue
                mask[i] = True
                if search(nums,mask,target,tmp_sum+nums[i],idx,i+1):
                    return True
                mask[i] = False
            return False
        return search(nums,mask,target,0,k,0)