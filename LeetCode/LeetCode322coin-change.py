#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 2:26 PM
# @Author  : Slade
# @File    : LeetCode322coin-change.py

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            min_value = float("inf")
            for coin in coins:
                if i >= coin:
                    min_value = min(min_value, 1 + dp[i - coin] if dp[i - coin] >= 0 else float("inf"))
            dp[i] = min_value if min_value != float("inf") else -1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([186, 419, 83, 408], 6249))
