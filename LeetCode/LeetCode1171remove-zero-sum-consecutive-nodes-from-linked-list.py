#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 4:36 PM
# @Author  : Slade
# @File    : LeetCode1171remove-zero-sum-consecutive-nodes-from-linked-list.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 补位
        node = ListNode(0)
        node.next = head
        hashmap = {0: node}
        tmp_sum = 0
        while head:
            tmp_sum += head.val
            if tmp_sum in hashmap.keys():
                hashmap[tmp_sum].next = head.next
                # 递归修正
                return self.removeZeroSumSublists(node.next)
            else:
                # 存储上一个结点
                hashmap[tmp_sum] = head
                head = head.next
        return node.next