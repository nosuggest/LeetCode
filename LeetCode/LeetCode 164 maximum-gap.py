#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 9:03 AM
# @Author  : Slade
# @File    : LeetCode 164 maximum-gap.py
class Bucket():
    def __init__(self, idx, min_value=float("inf"), max_value=-float("inf")):
        self.idx = idx
        self.min_value = min_value
        self.max_value = max_value
        self.values = []


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 桶个数要大于数组长度，必有一个控桶，最小最大值分布两侧，则单个桶内的极值必然小于N+1个桶内的极值
        if len(nums) < 2:
            return 0
        bucket_number = len(nums) + 1
        bucket_size = (max(nums) - min(nums)) / (bucket_number - 1)
        if bucket_size == 0:
            return 0

        # 构造好n+1个桶
        bucket_list = []
        start = min(nums)
        for i in range(bucket_number):
            bucket_list.append(Bucket(i))
            start += bucket_size

        # 放值入桶
        for num in nums:
            bucket_list[int((num - min(nums)) // bucket_size)].min_value = min(
                bucket_list[int((num - min(nums)) // bucket_size)].min_value, num)
            bucket_list[int((num - min(nums)) // bucket_size)].max_value = max(
                bucket_list[int((num - min(nums)) // bucket_size)].max_value, num)

        # 找出之间的最大间隔
        preMax = bucket_list[0].max_value
        max_diff = 0
        for i in range(1, len(bucket_list)):
            if bucket_list[i].min_value != float("inf"):
                max_diff = max(max_diff, bucket_list[i].max_value - preMax)
                preMax = bucket_list[i].max_value
        return max_diff

    def maximumGap1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        length = max(nums) + 1
        tmp = [0] * length
        for num in nums:
            tmp[num] = num
        tmp = [0] + tmp
        start = 0
        diff = 0
        for i in range(length + 1):
            if tmp[i] != 0:
                if tmp[i] - start > diff:
                    diff = tmp[i] - start
                if tmp[i - 1] == 0:
                    start = tmp[i]
        return diff


if __name__ == '__main__':
    s = Solution()
    print (s.maximumGap([1, 1, 1]))
