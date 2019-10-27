#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 8:49 PM
# @Author  : Slade
# @File    : LeetCode897increasing-order-search-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        queue = []
        ans = []
        cur = root
        while True:
            while cur:
                queue.append(cur)
                cur = cur.left
            if not queue:
                break
            cur = queue.pop()
            ans.append(cur.val)
            cur = cur.right
        root = TreeNode(ans[0])
        tmp = root
        for i in range(1, len(ans)):
            root.right = TreeNode(ans[i])
            root = root.right
        return tmp


