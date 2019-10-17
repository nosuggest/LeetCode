#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 11:42 PM
# @Author  : Slade
# @File    : LeetCode662maximum-width-of-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        tmp = {}  # 记录每层的序号

        def core(root, k, number):
            '''
            :param root:结点
            :param k: 层数
            :param number:序号
            :return:
            '''
            '''记录每层的序号'''
            if k not in tmp:
                tmp[k] = []
            tmp[k].append(number)
            if root.left:
                core(root.left, k + 1, number * 2)
            if root.right:
                core(root.right, k + 1, number * 2 + 1)
        '''最左侧都是以0开始，向右递增'''
        core(root, 0, 0)
        for x in tmp:
            res = max(res, tmp[x][len(tmp) - 1] - tmp[x][0])
        return res
