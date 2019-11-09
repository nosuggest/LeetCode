#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 1:13 PM
# @Author  : Slade
# @File    : 多重背包.py
def MultiplePack(N, V, weight, value, num):
    """
    多重背包问题(每个物品都有次数限制)
    :param N: 物品个数, 如 N=5
    :param V: 背包总容量, 如V=15
    :param weight: 每个物品的容量数组表示, 如weight=[5,4,7,2,6]
    :param value: 每个物品的价值数组表示, 如value=[12,3,10,3,6]
    :param num: 每个物品的个数限制，如num=[2,4,1,5,3]
    :return: 返回最大的总价值
    """
    dp = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, 1 + V):
            dp[i][j] = dp[i - 1][j]

            for k in range(min(num[i - 1], j // weight[i - 1]) + 1):
                if dp[i][j] < dp[i - 1][j - k * weight[i - 1]] + value[i - 1] * k:
                    dp[i][j] = dp[i - 1][j - k * weight[i - 1]] + value[i - 1] * k
    print(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    print(MultiplePack(5, 15, [5, 4, 7, 2, 6], [12, 3, 10, 3, 6], [2, 4, 1, 5, 3]))
