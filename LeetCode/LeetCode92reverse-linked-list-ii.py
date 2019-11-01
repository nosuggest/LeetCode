# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        node = ListNode(-1)
        node.next = head

        prev = node

        for i in range(m - 1):
            prev = prev.next

        # 反转点
        cur = prev.next
        tmp_prev = None
        # n-m+1长度
        for i in range(n - m + 1):
            tmp = cur.next
            cur.next = tmp_prev
            tmp_prev = cur
            cur = tmp
        # prev.next为待反转的结点，prev.next.next为反转后一个结点
        # prev.next为反转后的尾结点，正好可以接剩余结点
        prev.next.next = cur
        prev.next = tmp_prev
        return node.next
