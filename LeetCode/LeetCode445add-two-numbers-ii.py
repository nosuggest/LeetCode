#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 11:15 PM
# @Author  : Slade
# @File    : LeetCode445add-two-numbers-ii.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        stackl1 = []
        stackl2 = []

        while l1:
            stackl1.append(l1.val)
            l1 = l1.next
        while l2:
            stackl2.append(l2.val)
            l2 = l2.next
        # 补全
        if len(stackl1) > len(stackl2):
            stackl2 = [0] * (len(stackl1) - len(stackl2)) + stackl2
        else:
            stackl1 = [0] * (len(stackl2) - len(stackl1)) + stackl1

        dummy = None
        tmp1 = 0
        # 出栈
        for i in range(len(stackl1) - 1, -1, -1):
            node = ListNode((tmp1 + stackl1[i] + stackl2[i]) % 10)
            node.next = dummy
            dummy = node
            tmp1 = (tmp1 + stackl1[i] + stackl2[i]) // 10
        # 对最后的出栈值tmp1未来得及处理的进位数进行处理
        if tmp1:
            node = ListNode(tmp1 % 9)
            node.next = dummy
            dummy = node
        return dummy
