#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode 121 best-time-to-buy-and-sell-stock.py
@Author: sladesha
@Date  : 2019/8/13 21:47
@Desc  : 
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = 0
        min_price = float("inf")
        for i in range(0,len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            if prices[i]-min_price >diff:
                diff = prices[i]-min_price
        return diff