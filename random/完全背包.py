#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 1:03 PM
# @Author  : Slade
# @File    : 完全背包.py

def CompletePack(N, V, weight, value):
    """
    完全背包问题(每个物品可以取无限次)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :return: 返回最大的总价值
    """
    dp = [[0 for i in range(V + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, V + 1):
            # 初始话为当层不取，上一层的容量下的最大价值
            dp[i][j] = dp[i - 1][j]
            # 容量为j时，weight[j-1]最多可以取几次
            for k in range(j // weight[i - 1] + 1):
                # 只需要考虑可以重复拿几次的问题
                if dp[i - 1][j - k * weight[i - 1]] + k * value[i - 1] > dp[i][j]:
                    dp[i][j] = dp[i - 1][j - k * weight[i - 1]] + k * value[i - 1]
    print(dp)
    return dp[-1][-1]

if __name__ == '__main__':
    print(CompletePack(5,15,[5,4,7,2,6],[12,3,10,3,6]))