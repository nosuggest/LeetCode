#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 3:40 PM
# @Author  : Slade
# @File    : LeetCode1019next-greater-node-in-linked-list.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        dp = [0] * len(tmp)
        stack = []
        for k, v in enumerate(tmp):
            while stack and stack[-1][-1] < v:
                idx, val = stack.pop()
                dp[idx] = v
            stack.append((k, v))
        return dp

