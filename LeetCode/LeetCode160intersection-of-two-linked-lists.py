#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 7:56 PM
# @Author  : Slade
# @File    : LeetCode160intersection-of-two-linked-lists.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        ha = headA
        hb = headB

        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha