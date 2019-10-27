#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 2:51 PM
# @Author  : Slade
# @File    : LeetCode1008construct-binary-search-tree-from-preorder-traversal.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)

        def buildTree(preorder, inorder):
            if not preorder:
                return None
            if preorder:
                rootPoint = preorder[0]
                splitPoint = inorder.index(rootPoint)
                root = TreeNode(rootPoint)
                root.left = buildTree(preorder[1:1 + splitPoint], inorder[:splitPoint])
                root.right = buildTree(preorder[1 + splitPoint:], inorder[splitPoint + 1:])
                return root

        return buildTree(preorder, inorder)
