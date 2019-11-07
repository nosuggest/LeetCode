#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 2:10 PM
# @Author  : Slade
# @File    : LeetCode10regular-expression-matching.py
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s or not p:
            return False
        # ab & aa,[[f,f,f],[f,f,f],[f,f,f]]
        # 行为带匹配字符串
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                # 一致则延续上一次的状态
                if s[i] == p[j] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # 不一致观察是否为"*"
                    if p[j] == "*":
                        # 比较"*前是否一致，不一致则*必为0"，abc & ad*
                        if p[j - 1] != s[i] and p[j - 1] != ".":
                            # 把d*置空，考虑adc和a
                            dp[i + 1][j + 1] = dp[i + 1][j - 1]
                        else:
                            # abc & ac*,分三种情况再讨论，因为我们讨论范围是c和c*，所以只需要交叉考虑即可
                            # 不考虑*，abc和ac部分是否一致：dp[i + 1][j]
                            # 不考虑c*，abc和a部分是否一致： dp[i + 1][j - 1]
                            # 最复杂的最优子问题部分：ab和ac*是否一致，因为ab再加一个c完全不影响结果：dp[i][j + 1]
                            dp[i + 1][j + 1] = dp[i + 1][j] or dp[i + 1][j - 1] or dp[i][j + 1]
                            # 其他情况均为False
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isMatch("aab", "c*a*b."))
