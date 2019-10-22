#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode22generate-parentheses.py
@Author: sladesha
@Date  : 2019/10/22 23:55
@Desc  : 
'''

class Solution(object):
    def __init__(self):
        self.ans = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(s,letf,right):
            if letf == n and right==n:
                self.ans.append(s)

            if letf<n:
                dfs(s+"(",letf+1,right)

            if right<letf:
                dfs(s+")",letf,right+1)

        dfs("",0,0)
        return self.ans
