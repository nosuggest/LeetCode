#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 9:18 AM
# @Author  : Slade
# @File    : LeetCode1028recover-a-tree-from-preorder-traversal.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        depth = {-1: TreeNode(0)}

        def buildTree(val, high):
            depth[high] = TreeNode(int(val))

            if not depth[high - 1].left:
                depth[high - 1].left = depth[high]
            else:
                depth[high - 1].right = depth[high]

        value, par = "", 0
        for s in S:
            if s != "-":
                value += s
            elif value:
                buildTree(value, par)
                value, par = "", 1
            else:
                par += 1
        buildTree(value, par)
        return depth[0]

if __name__ == '__main__':
    s = Solution()
    s.recoverFromPreorder("1-2--3--4-5--6--7")
