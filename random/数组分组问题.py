#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 9:00 PM
# @Author  : Slade
# @File    : 数组分组问题.py
'''

给定一个时刻表，根据目的地进行分组，同一个目的地必须尽可能的多分，不能打乱顺序，比如aabbcddc，需要分成aa|bb|cddc,而不能分成aabb|cddc，因为这种情况下不是最多，也不能分成aa|bb|c|dd|c,因为相同的c没有被分在一起；求分组个数；

用了两种方法解，数组区间合并和动态规划
'''
# 动态规划
from collections import defaultdict


def get_result(nums):
    d = defaultdict(int)
    dp = [0] * len(nums)
    dp[0] = 1
    d[nums[0]] = 0
    for i in range(1, len(nums)):
        if nums[i] not in d.keys():
            dp[i] = dp[i - 1] + 1
            d[nums[i]] = i
        elif nums[i] == nums[i - 1]:
            dp[i] = dp[i - 1]
            d[nums[i]] = i
        else:
            lastindex = d.get(nums[i])
            minindex = float("inf")
            for j in range(lastindex, i):
                minindex = min(minindex, d.get(nums[j]))
            dp[i] = dp[minindex]
            d[nums[i]] = minindex
    return dp[-1]

# 区间合并
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) <= 1:
        return intervals
    res = []
    intervals = sorted(intervals, key=lambda start: start[0])
    l = intervals[0][0]
    h = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= h:
            h = max(h, intervals[i][1])
        else:
            res.append([l, h])
            l = intervals[i][0]
            h = intervals[i][1]
    res.append([l, h])
    return res


input_str = 'abdabcabdab'
unique_lst = list(set(list(input_str)))

intervals = []
for s in unique_lst:
    start, end = input_str.index(s), len(input_str) - input_str[::-1].index(s) - 1
    intervals.append([start, end])

result = merge(intervals)
interval_length = []
for interval in result:
    interval_length.append(str(interval[1] - interval[0] + 1))
