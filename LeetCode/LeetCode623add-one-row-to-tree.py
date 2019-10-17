#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 1:55 PM
# @Author  : Slade
# @File    : LeetCode623add-one-row-to-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return

        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        if d == 2:
            lnode = TreeNode(v)
            rnode = TreeNode(v)
            lnode.left, rnode.right, root.left, root.right = root.left, root.right, lnode, rnode
            '''return root 不能写在这里，因为self.addOneRow会进行调用，对root进行了修改，else里面并没有返回输出，导致返回None'''
        else:
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)
        return root
