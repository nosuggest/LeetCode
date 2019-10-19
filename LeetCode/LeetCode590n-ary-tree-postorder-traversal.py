#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 12:24 PM
# @Author  : Slade
# @File    : LeetCode590n-ary-tree-postorder-traversal.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        if not root:
            return None
            # return []

        for item in root.children:
            ans += self.postorder(item)

        ans += [root.val]
        return ans

    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        queue = [root]
        ans = []
        while queue:
            node = queue.pop()
            ans.append(node.val)
            for item in node.children:
                queue.append(item)
        return ans[::-1]
