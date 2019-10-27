#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 11:05 AM
# @Author  : Slade
# @File    : LeetCode100same-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        queue = [p, q]

        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1.val != t2.val:
                return False

            if t1.left is None and t2.left is None:
                pass
            elif t1.left is None or t2.left is None:
                return False
            else:
                queue.append(t1.left)
                queue.append(t2.left)

            if t1.right is None and t2.right is None:
                pass
            elif t1.right is None or t2.right is None:
                return False
            else:
                queue.append(t1.right)
                queue.append(t2.right)
        return True

