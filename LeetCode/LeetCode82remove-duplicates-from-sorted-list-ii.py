# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # 待修正链表
        tmp = ListNode(None)
        tmp.next = head

        # 判断是否有重复值的链表
        cur = tmp

        while cur:
            # 修改tmp的中间变量
            prev = cur
            # cur迭代的时候，prev是不变的
            cur = cur.next
            while cur and cur.next and cur.val == cur.next.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
            # 只修改cur最初循环开始的next指向
            prev.next = cur
        return tmp.next
