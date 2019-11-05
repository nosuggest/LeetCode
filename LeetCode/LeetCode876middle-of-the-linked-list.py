#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 3:03 PM
# @Author  : Slade
# @File    : LeetCode876middle-of-the-linked-list.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow