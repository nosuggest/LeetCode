# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        tmp = head
        while cur:
            prev = cur
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur.next
            cur = cur.next
        return tmp
