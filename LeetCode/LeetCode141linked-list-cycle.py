#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 7:21 PM
# @Author  : Slade
# @File    : LeetCode141linked-list-cycle.py
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        fast = head.next.next
        slow = head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True