#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 11:11 AM
# @Author  : Slade
# @File    : LeetCode23merge-k-sorted-lists.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''快排按照标值二分，小的在前大的在后，而归并则是按照下标二分，再分别对两个部分归并排序，先分后和，在和的过程中排序'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) >> 1
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwo(l1, l2)

    def mergeTwo(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        # 递归写法，栈内存更大
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwo(l1.next,l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwo(l1,l2.next)
        #     return l2

        # 迭代写法
        tmp = res = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next, l1 = l1, l1.next
            else:
                tmp.next, l2 = l2, l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return res.next
