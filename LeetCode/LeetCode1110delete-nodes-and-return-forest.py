#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 5:37 PM
# @Author  : Slade
# @File    : LeetCode1110delete-nodes-and-return-forest.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        delete = set(to_delete)
        ans = []
        if not root:
            return None

        if root.val not in to_delete:
            ans.append(root)

        def dfs(root):
            '''对root进行修改'''
            if not root:
                return

            left, right = root.left, root.right

            '''如果root需要被删除'''
            if root.val in delete:
                if left and left.val not in delete:
                    ans.append(left)
                if right and right.val not in delete:
                    ans.append(right)

            '''如果root.left需要被删除'''
            if left and left.val in delete:
                # 因为left结点，dfs(left)中进行计算
                root.left = None

            '''如果root.right需要被删除'''
            if right and right.val in delete:
                root.right = None

            dfs(left)
            dfs(right)

        dfs(root)
        return ans
