#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 4:39 PM
# @Author  : Slade
# @File    : LeetCode98validate-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []

        def inOrderTraverse(root):
            if root:
                inOrderTraverse(root.left)
                ans.append(root.val)
                inOrderTraverse(root.right)

        inOrderTraverse(root)
        return all([ans[i] < ans[i + 1] for i in range(len(ans) - 1)]) or False
