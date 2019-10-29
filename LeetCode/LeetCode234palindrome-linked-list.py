#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 2:03 PM
# @Author  : Slade
# @File    : LeetCode234palindrome-linked-list.py

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, prev = head, head, None

        while fast:
            fast = fast.next.next if fast.next else fast.next
            slow = slow.next

        while slow:
            # slow
            # 右侧slow, slow.next, prev分别会产生三个tmp变量，等号执行到左侧在进行映射对应

            # 以下两种都在完成prev和slow.next执行之前把slow给变更掉了
            # prev, slow, slow.next = slow, slow.next, prev
            # slow, slow.next, prev = slow.next, prev, slow

            # slow.next, slow, prev = prev, slow.next, slow

            '''
            以1->2->3->4->5为例：

                过程：

                res:None

                第一层循环

                res:1->2->3->4->5	res = p

                res:1->None	res.next = res

                p:2->3->4->5	p = p.next

                第二层循环

                res:2->3->4->5	res = p

                res:2->1->None	res.next = res

                p:3->4->5	p = p.next

                第三层循环

                res:3->4->5	res = p

                res:3->2->1->None	res.next = res

                p:4->5	p = p.next

                第四层循环

                res:4->5	res = p

                res:4->3->2->1->None	res.next = res

                p:5	p = p.next

                第五层循环

                res:5	res = p

                res:5->4->3->2->1->None	res.next = res

                p:None	p = p.next

                end...
            '''
            prev, prev.next, slow = slow, prev, slow.next

            '''
            等价于
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            '''

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
