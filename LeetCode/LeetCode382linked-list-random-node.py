#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 4:07 PM
# @Author  : Slade
# @File    : LeetCode382linked-list-random-node.py
from random import randint


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        head = self.head
        l = self.length
        while True:
            # l中可能，每次的概率均为1/l
            idx = randint(1, l)
            if idx == 1:
                return head.val
            head = head.next
            l -= 1
