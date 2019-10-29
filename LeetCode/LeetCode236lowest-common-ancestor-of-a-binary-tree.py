#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 7:59 PM
# @Author  : Slade
# @File    : LeetCode236lowest-common-ancestor-of-a-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
这行代码的背后：
1、left 来自于左子树查找p,q的结果，如果查到了返回对应，没有的话返回None
2、right 来自于右子树查找p,q的结果，如果查到了返回对应，没有的话返回None
3、如果分别来自左右子树，意味着left和right都不为None，则返回改root，即为最近的父结点
4、一旦查到，剩下的搜索结果都会为None，又回到了1，2两种情况

'''

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return left if right is None else right if left is None else root
