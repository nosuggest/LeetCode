# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        while head.val==val:
            head = head.next
            if not head:
                return head
        prob = head
        while prob.next:
            if prob.next.val==val:
                prob.next = prob.next.next
                if not prob.next:
                    break
            else:
                prob = prob.next
                if not prob.next:
                    break
        return head
            