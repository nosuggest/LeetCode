#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 7:03 PM
# @Author  : Slade
# @File    : LeetCode865smallest-subtree-with-all-the-deepest-nodes.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def search(root):
            if not root:
                return None, 0

            left = search(root.left)
            right = search(root.right)

            if left[1] > right[1]:
                return left[0], left[1] + 1
            elif left[1] < right[1]:
                return right[0], right[1] + 1
            else:
                return root, left[1] + 1

        return search(root)[0]
