#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 11:01 AM
# @Author  : Slade
# @File    : LeetCode687longest-univalue-path.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def search(root, val):
            if not root:
                return 0

            '''
            此处为逻辑处
            '''
            # 子叶结点，回程开始条件
            if not root.left and not root.right:
                return root.val == val

            # 递归到底层
            left = search(root.left, root.val)
            right = search(root.right, root.val)

            # 修正全局最大值
            self.ans = max(self.ans, left + right)

            # 以上算的都是子树的值，现在比较左右结点和当前结点是否一致
            if root.val == val:
                return max(left, right) + 1
            else:
                return 0

        search(root, root.val)
        return self.ans
