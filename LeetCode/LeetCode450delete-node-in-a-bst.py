#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:48 PM
# @Author  : Slade
# @File    : LeetCode450delete-node-in-a-bst.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        '''核心在于分三种情况处理：

            1、删除结点的左支为空
            2、删除结点的右支为空
            2、删除结点的左右支为非空，拿到比当前支大的最小的一个值，及右支最小值，递归删除
        '''
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                '''需要找一个比root.val的值大的最小值'''
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                root.val = tmp.val
                '''因为左树的右支的支被赋值到root.val了，需要把root.right中的刚才赋值的值删除'''
                root.right = self.deleteNode(root.right, tmp.val)
                return root
