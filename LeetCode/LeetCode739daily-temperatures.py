#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 10:01 AM
# @Author  : Slade
# @File    : LeetCode739daily-temperatures.py
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        dp = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            for j in range(i + 1, len(T)):
                if T[i] < T[j]:
                    dp[i] = j - i
                    break
                # 如果历史上的已经比当前的都小就不用再去比了，c++可以pass，python OOT.
                elif dp[j] == 0:
                    break
        return dp


class Solution1(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        dp = [0] * len(T)
        for k, v in enumerate(T):
            while stack and stack[-1][1] < v:
                ki, _ = stack.pop()
                dp[ki] = k - ki
            stack.append((k, v))
        return dp


if __name__ == '__main__':
    s = Solution1()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
