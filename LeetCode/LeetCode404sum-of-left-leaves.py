#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 3:05 PM
# @Author  : Slade
# @File    : LeetCode404sum-of-left-leaves.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        queue = [root]
        ans = 0
        while queue:
            node = queue.pop(0)  # 用的还是层序遍历
            if node.left and not node.left.left and not node.left.right:
                ans += node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans
