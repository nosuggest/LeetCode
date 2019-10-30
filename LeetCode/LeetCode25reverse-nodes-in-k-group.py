#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 1:29 PM
# @Author  : Slade
# @File    : LeetCode25reverse-nodes-in-k-group.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 小于k的链表部分不需要翻转
        check = head
        check_length = 0
        while check:
            check_length += 1
            check = check.next

        if check_length < k: return head

        # 翻转开始，只是这边需要k次，不是24题的两次
        swap_times = k
        cur = head
        prev = None
        while swap_times > 0 and cur:
            # 保存下一个位置，进行下一轮迭代
            tmp = cur.next
            # 两两交换的话这边是好tmp.next构造1-3-4，逆序的话构造的是2-1-None
            # 此处head结点也被修改了，head.next也为prev了
            cur.next = prev
            # 此处prev、cur、head地址一致
            prev = cur
            cur = tmp
            swap_times -= 1
        if tmp:
            # 上面说head结点也被修改了，head.next为None是翻转后的尾结点，直接拼接剩下来的reverseKGroup(cur, k)即可
            head.next = self.reverseKGroup(cur, k)
        return prev
