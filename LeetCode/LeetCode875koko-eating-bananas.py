#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 5:11 PM
# @Author  : Slade
# @File    : LeetCode875koko-eating-bananas.py

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        '''向上取整的实现方式(x-1)//k+1'''
        if len(piles) == 1:
            return (piles[0] - 1) // H + 1

        def isMatch(val):
            return sum([(i - 1) // val + 1 for i in piles]) <= H

        left = (sum(piles) - 1) // H + 1
        right = max(piles)
        while left < right:
            mid = (left + right) >> 1
            if not isMatch(mid):
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([2, 2, 2, 2], 4))
