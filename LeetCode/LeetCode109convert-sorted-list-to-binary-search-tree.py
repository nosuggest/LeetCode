# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)


        start = prev = slow = fast = head


        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        mid = slow.val
        prev.next = None
        Node = TreeNode(mid)

        Node.left = self.sortedListToBST(start)
        Node.right = self.sortedListToBST(slow.next)
        return Node


# Definition for singly-linked list.
class ListNode1(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode2(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution3(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        fast = head
        slow = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node
