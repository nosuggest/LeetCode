# coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # left:head
        # right:slow
        right = self.resverse(slow.next)
        slow.next = None

        left = head
        while left and right:
            l2 = right
            right = right.next

            # 3->2
            l2.next = left.next
            # 1->3->2
            left.next = l2
            left = left.next.next

    def resverse(self, slow):
        if not slow or not slow.next:
            return slow
        tmp_prev = None
        while slow:
            tmp = slow.next
            slow.next = tmp_prev
            tmp_prev = slow
            slow = tmp
        return tmp_prev

