#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 7:34 PM
# @Author  : Slade
# @File    : LeetCode872leaf-similar-trees.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def search(root):
            ans = []
            if not root:
                return None
            if not root.left and not root.right:
                return [root.val]
            if root.left:
                ans += search(root.left)
            if root.right:
                ans += search(root.right)
            return ans

        return search(root1) == search(root2)