#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 9:11 PM
# @Author  : Slade
# @File    : LeetCode124binary-tree-maximum-path-sum.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = -float("inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def help(root):
            if not root:
                return 0

            left = help(root.left)
            right = help(root.right)

            # 考虑当前结点是否可以作为根结点通过的情况下，需要考虑全局最优的大小
            self.ans = max(self.ans, left + right + root.val)

            # 考虑当前结点作为下一次迭代结点的时候，选左支还是右支
            return max(0, max(left, right) + root.val)

        help(root)
        return self.ans
