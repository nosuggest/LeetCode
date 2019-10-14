#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 1:43 PM
# @Author  : Slade
# @File    : LeetCode99recover-binary-search-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.inOrderTraverse(root)
        node1 = None
        node2 = None
        for i in range(len(self.ans) - 1):
            if self.ans[i].val > self.ans[i + 1].val and node1 == None:
                node1 = self.ans[i]
                node2 = self.ans[i + 1]
            elif self.ans[i].val > self.ans[i + 1].val and node1 != None:
                node2 = self.ans[i + 1]
        node1.val, node2.val = node2.val, node1.val

    def inOrderTraverse(self, root):
        if root:
            self.inOrderTraverse(root.left)
            self.ans.append(root)
            self.inOrderTraverse(root.right)
