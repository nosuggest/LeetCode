#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 10:04 AM
# @Author  : Slade
# @File    : LeetCode671second-minimum-node-in-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def search(root, val):
            if not root:
                return -1

            '''跳出条件'''
            if root.val > val:
                return root.val

            left = search(root.left, val)
            right = search(root.right, val)

            '''
            max(root.val, min(left, right))这边是错的，应该是max(left, right)
            首先，题目中指出，叶子结点会更大，所以root.val<=left,right，第二大的数必定在left, right中
            其次，left, right可能会出现-1，min不合适
            '''
            return min(left, right) if left > root.val and right > root.val else max(left, right)

        return search(root, root.val)
