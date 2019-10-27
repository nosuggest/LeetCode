#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 8:13 PM
# @Author  : Slade
# @File    : LeetCode107binary-tree-level-order-traversal-ii.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        queue = [root]
        tmp = [root]
        length = 1
        lengths = [1]
        while tmp:
            for _ in range(length):
                root = tmp.pop(0)
                if root.right:
                    tmp.append(root.right)
                    queue.append(root.right)
                if root.left:
                    tmp.append(root.left)
                    queue.append(root.left)

            length = len(tmp)
            if length:
                lengths.append(length)
        lengths = lengths[::-1]
        queue = queue[::-1]

        ans = []
        for length in lengths:
            tmp = []
            for _ in range(length):
                item = queue.pop(0)
                tmp.append(item.val)
            ans.append(tmp)
        return ans