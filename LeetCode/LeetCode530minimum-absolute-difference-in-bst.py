#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 12:03 AM
# @Author  : Slade
# @File    : LeetCode530minimum-absolute-difference-in-bst.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        stack = []
        ans=[]
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            tmp = stack.pop()
            ans.append(tmp.val)
            node = tmp.right
        return min([abs(ans[i]-ans[i+1]) for i in range(len(ans)-1)])