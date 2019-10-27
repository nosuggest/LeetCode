#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 8:44 PM
# @Author  : Slade
# @File    : LeetCode226invert-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if not root:
            # 保证搜索到最低层的时候进行原值返回即可
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
