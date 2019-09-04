#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 9:00 PM
# @Author  : Slade
# @File    : 数组分组问题.py

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
