#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 9:27 AM
# @Author  : Slade
# @File    : LeetCode105construct-binary-tree-from-preorder-and-inorder-traversal.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        split_point = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:split_point + 1], inorder[:split_point])
        root.right = self.buildTree(preorder[split_point + 1:], inorder[split_point + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([1, 2], [1, 2])
