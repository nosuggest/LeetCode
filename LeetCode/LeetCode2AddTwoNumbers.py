#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:52 AM
# @Author  : Slade
# @File    : LeetCode2AddTwoNumbers.py

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
        l1_list = []
        while l1 != None:
            l1_list.append(l1.val)
            l1 = l1.next

        l2_list = []
        while l2 != None:
            l2_list.append(l2.val)
            l2 = l2.next

        if len(l1_list) > len(l2_list):
            l2_list = l2_list + [0] * (len(l1_list) - len(l2_list))
        else:
            l1_list = l1_list + [0] * (len(l2_list) - len(l1_list))

        ans = [l1_list[i] + l2_list[i] for i in range(len(l1_list))]

        for i in range(len(ans) - 1):
            if ans[i] >= 10:
                ans[i] = ans[i] - 10
                ans[i + 1] = ans[i + 1] + 1
        if ans[len(ans) - 1] >= 10:
            ans[len(ans) - 1] = ans[len(ans) - 1] - 10
            ans.append(1)

        head = probe = ListNode(ans[0])
        for i in ans[1:]:
            probe.next = ListNode(i)
            probe = probe.next
        return head


if __name__ == "__main__":
    l1 = l3 = ListNode(9)
    for i in [8]:
        l3.next = ListNode(i)
        l3 = l3.next
    l2 = l4 = ListNode(1)
    for i in []:
        l4.next = ListNode(i)
        l4 = l4.next

    s = Solution()
    print(s.addTwoNumbers(l1, l2).val)
