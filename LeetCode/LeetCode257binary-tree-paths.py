#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 2:09 PM
# @Author  : Slade
# @File    : LeetCode257binary-tree-paths.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def dfs(root, s):
            if not root:
                return
            if not root.left and not root.right:
                if s == "":
                    self.ans.append(str(root.val))
                else:
                    self.ans.append(s + "->" + str(root.val))
            if root.left:
                dfs(root.left, s + "->" + str(root.val) if s != "" else str(root.val))
            if root.right:
                dfs(root.right, s + "->" + str(root.val) if s != "" else str(root.val))

        dfs(root, "")
        return self.ans
