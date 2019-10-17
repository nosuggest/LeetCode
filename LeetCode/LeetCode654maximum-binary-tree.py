#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 10:06 PM
# @Author  : Slade
# @File    : LeetCode654maximum-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxValue = max(nums)
        split_part = nums.index(maxValue)
        root = TreeNode(maxValue)
        root.left = self.constructMaximumBinaryTree(nums[:split_part])
        root.right = self.constructMaximumBinaryTree(nums[split_part + 1:])
        return root
