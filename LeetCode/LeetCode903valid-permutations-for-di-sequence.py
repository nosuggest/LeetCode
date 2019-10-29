#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode903valid-permutations-for-di-sequence.py.py
@Author: sladesha
@Date  : 2019/9/11 0:14
@Desc  : 
'''


'''
>这边需要明白一个规则，举个例子：S:[0,1,2,3],P:[DID];dp[i,j]中i指S中的最大范围，此处i最大=3，j为以什么为结尾
dp[2.1]则为S:[0,1,2],且以1为结尾，因为p为DID，所以当i=2的时候，应该满足DI，1为结尾，又因为I为此时P的结尾，所以
[0,1]的前两位组合的末尾应该是比二小就行，所以d[1,1]和dp[1,0]都行，dp[2,2] = dp[1,0]+dp[1,1]=1+0；如果是ID的情况
同上，所以状态转移方程应该是：
if S[i-1] == "D":dp[i,j] += dp[i-1,k] j<=k<=i-1
if S[i-1] == "I":dp[i,j] += dp[i-1,k] k<j
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