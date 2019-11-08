#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 3:39 PM
# @Author  : Slade
# @File    : LeetCode188best-time-to-buy-and-sell-stock-iv.py

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        if k > len(prices) >> 1:
            tmp_sum = 0
            tmp_start = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < prices[i - 1]:
                    tmp_sum += prices[i - 1] - tmp_start
                    tmp_start = prices[i]

                if prices[i] >= prices[i - 1] and len(prices) - 1 == i:
                    tmp_sum += prices[i] - tmp_start
            return tmp_sum
        else:
            dp = [[-prices[0], 0] for _ in range(len(prices))]
            for price in prices[1:]:
                for i in range(1, k + 1):
                    dp[i] = [max(dp[i][0], dp[i - 1][1] - price), max(dp[i][1], dp[i][0] + price)]
            return dp[k][1]


if __name__ == '__main__':
    print(Solution().maxProfit(5, [3, 2, 6, 5, 0, 3]))
