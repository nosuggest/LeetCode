#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 7:36 PM
# @Author  : Slade
# @File    : LeetCode894all-possible-full-binary-trees.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        hashMap = {0: [], 1: [TreeNode(0)]}

        def dp(N):
            if N in hashMap:
                return hashMap[N]
            # dp循环

            ans = []
            for n in range(N):
                '''left结点个数+right结点个数=n-1，有一个需要是root根结点'''
                for left in dp(n):
                    for right in dp(N - n - 1):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            hashMap[N] = ans
            return ans

        dp(N)
        return hashMap[N]
