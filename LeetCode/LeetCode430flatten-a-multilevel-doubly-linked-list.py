#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 10:27 AM
# @Author  : Slade
# @File    : LeetCode430flatten-a-multilevel-doubly-linked-list.py

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        dummy = head
        pre = Node(-1, None, None, None)
        tmp = pre
        stack = [dummy]
        while stack:
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            tmp.next = node
            # 处理next
            # 处理prev
            # 处理child
            tmp, tmp.prev, node.child = tmp.next, tmp, None
        if pre.next:
            pre.next.prev = None
        return pre.next
