#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 10:31 PM
# @Author  : Slade
# @File    : LeetCode102binary-tree-level-order-traversal.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        ans = []
        queue.append(root)
        while queue:
            length = len(queue)
            tmp = []
            for _ in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(tmp)
        return ans


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []

        def helper(root, depth):
            if not root:
                return
            # 第一次便利到depth
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root,0)
        return ans
