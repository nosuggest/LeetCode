#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 8:51 PM
# @Author  : Slade
# @File    : LeetCode117populating-next-right-pointers-in-each-node-ii.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        queue = [root]

        while queue:
            length = len(queue)
            for idx in range(length):
                cur = queue.pop(0)
                if idx > 0:
                    pre.next = cur
                pre = cur

                if pre.left:
                    queue.append(pre.left)
                if pre.right:
                    queue.append(pre.right)
        return root
