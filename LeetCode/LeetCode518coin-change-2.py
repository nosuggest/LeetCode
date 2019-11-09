#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 9:43 PM
# @Author  : Slade
# @File    : LeetCode518coin-change-2.py
from typing import List


# 很不幸超时
class Solution1:
    def __init__(self):
        self.count = 0

    def change(self, amount: int, coins: List[int]) -> int:
        size = len(coins)
        self.dfs(coins, 0, size, amount, 0)
        return self.count

    def dfs(self, coins, start, size, amount, tmp_sum):
        if tmp_sum > amount:
            return
        if tmp_sum == amount:
            self.count += 1
            return
        for i in range(start, size):
            self.dfs(coins, i, size, amount, tmp_sum + coins[i])


# dp
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().change(10, [10]))
