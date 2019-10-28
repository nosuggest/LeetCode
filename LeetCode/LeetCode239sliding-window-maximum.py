#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 9:47 PM
# @Author  : Slade
# @File    : LeetCode239sliding-window-maximum.py

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums * k == 0:
            return []

        if k == 1:
            return nums
        deq = []

        def clean(i):
            # 删除最左侧值
            if deq and deq[0] == i - k:
                deq.pop(0)

            # 删除小于i位置的deq里面的值
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # 初始化
        max_idx = 0
        for i in range(k):
            clean(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        out = [nums[max_idx]]

        for i in range(k, len(nums)):
            clean(i)
            deq.append(i)
            out.append(nums[deq[0]])
        return out

if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))