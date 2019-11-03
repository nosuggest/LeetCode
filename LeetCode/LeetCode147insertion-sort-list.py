#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 9:29 PM
# @Author  : Slade
# @File    : LeetCode147insertion-sort-list.py
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            lat = cur.next
            if lat and cur.val > lat.val:
                while pre and pre.next.val < lat.val:
                    pre = pre.next
                # 待插入结点后的结点位置
                tmp = pre.next
                # 插入位置
                pre.next = lat
                # 把移走的lat结点前后连接起来
                cur.next = lat.next
                # tmp中的lat结点已经被移走了，所以只需要把tmp接入到lat.next后面即可
                lat.next = tmp

                pre = dummy
            else:
                cur = lat
        return head
