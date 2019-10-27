#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 11:12 AM
# @Author  : Slade
# @File    : LeetCode572subtree-of-another-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        return self.sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, queue, check):
        if queue is None and check is None:
            return True

        if queue is None or check is None:
            return False

        return queue.val == check.val and self.sameTree(queue.left, check.left) and self.sameTree(queue.right,
                                                                                                  check.right)
