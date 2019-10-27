#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 8:30 PM
# @Author  : Slade
# @File    : LeetCode116populating-next-right-pointers-in-each-node.py

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

        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
        return root
