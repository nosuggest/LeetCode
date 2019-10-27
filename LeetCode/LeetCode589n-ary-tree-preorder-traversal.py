#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 12:02 PM
# @Author  : Slade
# @File    : LeetCode589n-ary-tree-preorder-traversal.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    '''递归'''

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        ans = [root.val]

        children = root.children
        for child in children:
            ans += self.preorder(child)

        return ans

    '''迭代'''

    def preorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        ans = []
        queue = [root]
        while queue:
            node = queue.pop()
            ans.append(node.val)
            for item in node.children[::-1]:
                queue.append(item)
        return ans
