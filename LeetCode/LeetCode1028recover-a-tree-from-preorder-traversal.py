#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode1028recover-a-tree-from-preorder-traversal.py
@Author: sladesha
@Date  : 2019/10/21 22:52
@Desc  : 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        depth = {-1: TreeNode(0)}

        def addTree(v, p):
            depth[p] = TreeNode(int(v))

            if not depth[p - 1].left:
                depth[p - 1].left = depth[p]
            else:
                depth[p - 1].right = depth[p]

        val, p = "", 0
        for  c in S:
            if  c !="-":
                val+=c
            elif val:
                addTree(val,p)
                val,p="",1
            else:
                p+=1
        addTree(val,p)
        return depth[0]