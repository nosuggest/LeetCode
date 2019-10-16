#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 11:33 PM
# @Author  : Slade
# @File    : LeetCode501find-mode-in-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        queue = [root]
        ans = {}
        while queue:
            node = queue.pop()
            ans[node.val]=ans.get(node.val,0)+1
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        tmp = max(ans.values())
        return list(map(lambda x:x[0],filter(lambda x:x[1]==tmp,ans.items())))