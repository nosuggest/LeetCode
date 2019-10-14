#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 11:38 AM
# @Author  : Slade
# @File    : LeetCode103binary-tree-zigzag-level-order-traversal.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        tmp = 0
        queue = [root]
        length = len(queue)

        while queue:
            tmp_ans = []
            for _ in range(length):
                root = queue.pop(0)
                tmp_ans.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

            if tmp == 0:
                ans.append(tmp_ans)
                tmp = 1
            else:
                ans.append(tmp_ans[::-1])
                tmp = 0
            length = len(queue)
        return ans
