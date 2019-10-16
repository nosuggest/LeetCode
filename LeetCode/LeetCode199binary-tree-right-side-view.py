#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 11:55 AM
# @Author  : Slade
# @File    : LeetCode199binary-tree-right-side-view.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        output=[]
        queue = [root]
        length = 1
        while queue:
            tmp = 0
            for _ in range(length):
                node = queue.pop(0)
                tmp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length = len(queue)
            output.append(tmp)
        return output