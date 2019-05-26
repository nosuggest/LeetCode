# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next):
        self.val = x
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 如果是删除第一个
        length = 1
        probe = head
        while probe.next:
            length +=1
            probe = probe.next
        n = length - n + 1
        if n == 1 or head.next is None:
            head = head.next
        else:
            n = n - 1
            probe = head
            while n > 1:
                probe = probe.next
                n -= 1
            probe.next = probe.next.next

        return head