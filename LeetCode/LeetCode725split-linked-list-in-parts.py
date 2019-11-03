#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 11:23 PM
# @Author  : Slade
# @File    : LeetCode725split-linked-list-in-parts.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            length = 0
        else:
            length = 0
            check = root
            while check:
                length += 1
                check = check.next
        # 每组至少要分几个
        split_part = length // k
        # 有几组需要分split_part+1个
        split_more = length % k
        ans = []
        for _ in range(k):
            if root:
                cnt = split_part + (1 if split_more > 0 else 0)
                split_more -= 1
                ans.append(root)
                while (cnt - 1) > 0:
                    root = root.next
                    cnt -= 1
                tmp = root.next
                root.next = None
                root = tmp
            else:
                ans.append(None)
        return ans
