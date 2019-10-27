#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 1:21 PM
# @Author  : Slade
# @File    : 01背包.py

import numpy as np


def dp(weight, count, weights, costs):
    goods = [[0 for _ in range(weight + 1)] for _ in range(count + 1)]
    for i in range(1, count + 1):
        for j in range(1, weight + 1):
            goods[i][j] = goods[i - 1][j]
            if weights[i - 1] <= j and goods[i][j] < goods[i - 1][j - weights[i - 1]] + costs[i - 1]:
                goods[i][j] = goods[i - 1][j - weights[i - 1]] + costs[i - 1]
    return goods

def bags(w,c,ws,v):
    dp=[[0 for i in range(w+1)] for j in range(c+1)]

    for i in range(1,c+1):
        for j in range(1,w+1):
            if ws[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-ws[i-1]]+v[i-1],dp[i-1][j])
    return dp



if __name__ == '__main__':
    print(np.array(bags(12, 6, [4, 6, 2, 2, 5, 1], [8, 10, 6, 3, 7, 2])))
    print(np.array(dp(12, 6, [4, 6, 2, 2, 5, 1], [8, 10, 6, 3, 7, 2])))
