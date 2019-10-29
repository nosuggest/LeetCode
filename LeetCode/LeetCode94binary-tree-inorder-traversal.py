#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 9:20 PM
# @Author  : Slade
# @File    : LeetCode94binary-tree-inorder-traversal.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
三种写法：
1、好理解的递归
2、qsort递归写法
3、利用栈性质的迭代写法
'''
# 最好理解的写法
class Solution(object):
    def __init__(self):
        self.ans = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
        return self.ans


# qsort写法
class Solution1(object):
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# 迭代
# 利用栈去写
class Solution2(object):
    def inorderTraversal(self, root):
        r, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return r
            node = stack.pop()
            r.append(node.val)
            root = node.right
        return r
