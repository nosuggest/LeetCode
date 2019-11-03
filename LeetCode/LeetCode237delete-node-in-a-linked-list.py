#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 10:06 PM
# @Author  : Slade
# @File    : LeetCode237delete-node-in-a-linked-list.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next
