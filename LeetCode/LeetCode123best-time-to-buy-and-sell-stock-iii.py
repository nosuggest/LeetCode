#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 11:11 AM
# @Author  : Slade
# @File    : LeetCode123best-time-to-buy-and-sell-stock-iii.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        minval = prices[0]
        maxval = prices[-1]

        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], prices[i] - minval)
            minval = min(minval, prices[i])

        for i in range(n - 2, -1, -1):
            dp2[i] = max(dp2[i + 1], maxval - prices[i])
            maxval = max(maxval, prices[i])

        dp = [dp1[i] + dp2[i] for i in range(n)]

        return max(dp)


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
