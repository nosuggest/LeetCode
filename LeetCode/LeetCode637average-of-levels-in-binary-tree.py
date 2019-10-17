#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 4:36 PM
# @Author  : Slade
# @File    : LeetCode637average-of-levels-in-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None

        queue = [root]
        ans = []
        while queue:
            length = len(queue)
            tmp = []
            for i in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum(tmp)/len(tmp) if len(tmp) else 0)
        return ans