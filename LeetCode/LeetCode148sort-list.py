#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode148sort-list.py
@Author: sladesha
@Date  : 2019/10/29 22:23
@Desc  : 
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 跳出条件
        if not head or not head.next:
            return head

        # 中间切开
        fast, slow = head.next, head

        # fast and fast.next是找终点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid, slow.next = slow.next, None

        # cut and sort
        left, right = self.sortList(head), self.sortList(mid)

        # rank part
        # tmp 进行计算，res做最后的输出
        tmp = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                tmp.next, left = left, left.next
            else:
                tmp.next, right = right, right.next
            tmp = tmp.next

        tmp.next = left if left else right
        return res.next


