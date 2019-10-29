#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 9:37 PM
# @Author  : Slade
# @File    : LeetCode437path-sum-iii.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
>这题leetcode认为是简单，但是我觉得贼难：
1、python闭包的理解，count虽然是局部遍历，但是在递归的时候，每个count都是独立的
2、dfs(root.？？？？？, sum - root.val)用的是两数之和的逻辑进行递归
3、dfs(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
这个用的是遍历所有结点的方法

换句话说，这题解法是函数用递归实现，函数体是另外一个递归真的有点恶心
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root, sum):
            count = 0
            if not root:
                return 0
            if sum == root.val:
                count = 1

            count += dfs(root.left, sum - root.val)
            count += dfs(root.right, sum - root.val)

            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
