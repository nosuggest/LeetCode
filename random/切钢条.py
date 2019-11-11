#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 6:51 PM
# @Author  : Slade
# @File    : 切钢条.py

'''
问题：钢条切割
   给定长度为n英寸的钢条，和一个价格表P{1....n}，求切割钢条的方案，使得收益R最大。如果钢条价格足够大，可以完全不用切割。
'''


def get_ans(prices):
    length = len(prices)
    dp = [0] * (length + 1)
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + prices[j - 1])
    return dp[-1]


if __name__ == '__main__':
    print(get_ans([1, 5, 8, 16, 10, 17, 17, 20, 24, 30]))
