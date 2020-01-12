#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode134gas-station.py
@Author: sladesha
@Date  : 2020/1/12 16:00
@Desc  : 
'''


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        max_profit = -1
        total_profit = 0
        start = -1
        for i in range(len(gas) - 1, -1, -1):
            total_profit += gas[i] - cost[i]
            if total_profit > max_profit:
                max_profit = total_profit
                start = i
        if total_profit < 0:
            return -1
        return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4]
    cost = [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1]
    print (Solution().canCompleteCircuit(gas, cost))
