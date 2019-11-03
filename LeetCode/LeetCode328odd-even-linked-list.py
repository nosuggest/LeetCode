#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 10:28 PM
# @Author  : Slade
# @File    : LeetCode328odd-even-linked-list.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, pre1 = head, head.next
        p, p1 = pre, pre1

        while pre.next and pre1.next:
            pre.next, pre1.next = pre.next.next, pre1.next.next
            pre, pre1 = pre.next, pre1.next

        pre.next = p1
        return p
