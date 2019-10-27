#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 7:08 PM
# @Author  : Slade
# @File    : LeetCode106construct-binary-tree-from-inorder-and-postorder-traversal.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not postorder:
            return None

        # 找到根节点即可
        root = TreeNode(postorder[-1])
        split_point = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:split_point], postorder[:split_point])
        root.right = self.buildTree(inorder[split_point + 1:], postorder[split_point:-1])

        return root