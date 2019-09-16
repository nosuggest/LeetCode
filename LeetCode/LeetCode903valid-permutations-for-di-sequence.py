#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode903valid-permutations-for-di-sequence.py.py
@Author: sladesha
@Date  : 2019/9/11 0:14
@Desc  : 
'''

from functools import lru_cache


class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return 1
            elif S[i - 1] == "D":
                return sum(dp(i - 1, k) for k in range(j, i)) % MOD
            else:
                return sum(dp(i - 1, k) for k in range(j)) % MOD

        return sum(dp(length, k) for k in range(length + 1)) % MOD

if __name__ == '__main__':
    s = Solution()
    print(s.numPermsDISequence("DID"))