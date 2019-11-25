#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 10:43 AM
# @Author  : Slade
# @File    : 切分近似数组.py

'''
数组中的数分为两组，给出一个算法，使得两个组的和的差的绝对值最小数组中的数的取值范围是0<x<100，元素个数也是大于0，小于100
比如a[]={2,4,5,6,7},得出的两组数{2，4,，6}和{5，7}，abs(sum(a1)-sum(a2))=0;
比如{2，5，6，10}，abs(sum(2,10)-sum(5,6))=1,所以得出的两组数分别为{2，10}和{5,，6}。
'''

def bags(nums):
    weights = nums
    values = nums
    C = int(sum(nums) / 2) + 1
    dp = [[0 for i in range(C)] for j in range(len(nums) + 1)]
    for i in range(1, len(nums) + 1):
        for j in range(1, C):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp


def get_details(nums):
    res = bags(nums)
    x = [0] * (len(nums) + 1)
    j = int(sum(nums) / 2)
    for i in range(len(nums), 0, -1):
        if res[i][j] != res[i - 1][j]:
            x[i] = 1
            j -= nums[i - 1]
    ans = []
    for i, j in zip(nums, x[1:]):
        if j != 0:
            ans.append(i)
    return ans
