#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 8:07 PM
# @Author  : Slade
# @File    : LeetCode142linked-list-cycle-ii.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast = head.next.next
        slow = head.next
        while fast != slow:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
        start = head
        while start != slow:
            start = start.next
            slow = slow.next
        return start