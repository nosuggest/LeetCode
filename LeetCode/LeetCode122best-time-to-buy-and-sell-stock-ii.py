#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode122best-time-to-buy-and-sell-stock-ii.py
@Author: sladesha
@Date  : 2019/8/13 21:50
@Desc  : 
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        sumProfit = 0
        start_val = prices[0]
        for idx in range(1, len(prices)):
            if (prices[idx] < prices[idx - 1]):
                sumProfit += prices[idx - 1] - start_val
                start_val = prices[idx]
            if prices[idx] >= prices[idx - 1] and idx == len(prices)-1:
                sumProfit += prices[idx] - start_val
        return sumProfit

if __name__ == '__main__':
    s = Solution()
    print (s.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9]))