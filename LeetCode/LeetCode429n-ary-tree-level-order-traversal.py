#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 10:29 PM
# @Author  : Slade
# @File    : LeetCode429n-ary-tree-level-order-traversal.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return None
        ans = []
        queue = [root]
        while queue:
            length = len(queue)
            tmp = []
            for i in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.children:
                    for k in node.children:
                        queue.append(k)
            ans.append(tmp)
        return ans