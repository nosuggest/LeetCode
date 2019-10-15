#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 7:12 PM
# @Author  : Slade
# @File    : LeetCode114flatten-binary-tree-to-linked-list.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        while root is not None:

            if root.left is None:
                root = root.right
            else:

                '''左子树最大值必在右支上'''
                pre = root.left
                while pre.right is not None:
                    pre = pre.right

                pre.right = root.right
                '''结点被覆盖之前已经被转移到了左子树最大值上了'''
                root.right = root.left
                root.left = None

                root = root.right
