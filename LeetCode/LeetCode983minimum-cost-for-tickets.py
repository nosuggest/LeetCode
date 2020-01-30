#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 10:14 AM
# @Author  : Slade
# @File    : LeetCode983minimum-cost-for-tickets.py

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        l = max(days) + 1
        dp = [0] * l
        for i in range(1, l):
            if i not in days:
                dp[i] += dp[i - 1]
                continue
            dp[i] = min(dp[i - 1] + costs[0] if i - 1 >= 0 else costs[0],
                        dp[i - 7] + costs[1] if i - 7 >= 0 else costs[1],
                        dp[i - 30] + costs[2] if i - 30 >= 0 else costs[2])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))
