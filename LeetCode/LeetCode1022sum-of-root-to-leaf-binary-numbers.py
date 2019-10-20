#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 3:02 PM
# @Author  : Slade
# @File    : LeetCode1022sum-of-root-to-leaf-binary-numbers.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def search(root, s):
            tmp = s + str(root.val)
            if not root.left and not root.right:
                self.ans.append(tmp)
                return
            if root.left:
                search(root.left, tmp)
            if root.right:
                search(root.right, tmp)

        search(root, "")
        return sum([int(item,2)%(10**9 + 7) for item in self.ans])