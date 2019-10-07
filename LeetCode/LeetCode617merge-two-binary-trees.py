#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 12:07 AM
# @Author  : Slade
# @File    : LeetCode617merge-two-binary-trees.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            # return t1
        return t1 or t2  # t1 or t2当t1和t2都非空的时候，会先返回t1
