#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 2:44 PM
# @Author  : Slade
# @File    : LeetCode817linked-list-components.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0

        hashmap = {}
        for i in G:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        while head:
            while head and hashmap.get(head.val):
                hashmap[head.val] -= 1
                head = head.next
            count += 1
            head = head.next if head else head
        return count
