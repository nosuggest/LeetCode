#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 10:08 AM
# @Author  : Slade
# @File    : LeetCode61rotate-list.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        check = tmp = head
        length = 1
        while check.next:
            length += 1
            check = check.next
        check.next = head
        move = k % length
        move_step = length - move - 1
        while move_step > 0 and tmp:
            tmp = tmp.next
            move_step -= 1
        res = tmp.next
        tmp.next = None
        return res
