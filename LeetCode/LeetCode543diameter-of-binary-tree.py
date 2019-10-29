#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 10:59 PM
# @Author  : Slade
# @File    : LeetCode543diameter-of-binary-tree.py

# Definition for a binary tree node.
'''
比较坑的点：只有一个结点的时候，该题认为点重合，距离为0
做题思路就是：遍历所有结点，保存所有结点作为根结点的情况下，左右子树的最大深度和即可


'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.maxDepth = 0

        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            self.maxDepth = max(self.maxDepth, L + R)#左右树深度之和
            return max(L, R) + 1

        depth(root)
        return self.maxDepth


class tree:
    def __init__(self, l):
        self.root = TreeNode(l[0])
        for i in l[1:]:
            self.insert(i)

    def search(self, value, node, parent):
        if node is None:
            return False, node, parent

        if value == node.val:
            return True, node, parent

        if value > node.val:
            return self.search(value, node.right, node)
        else:
            return self.search(value, node.left, node)

    def insert(self, data):
        flag, n, p = self.search(data, self.root, self.root)
        if not flag:
            if p.val > data:
                p.left = TreeNode(data)
            else:
                p.right = TreeNode(data)

    def preOrderTraverse(self, node):
        if node is not None:
            print(node.val)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)

    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.left)
            print(node.val)
            self.inOrderTraverse(node.right)

    def posOrderTraverse(self, node):
        if node is not None:
            self.posOrderTraverse(node.left)
            self.posOrderTraverse(node.right)
            print (node.val)


if __name__ == '__main__':
    t = tree([4, 2, 1, 3, 5])
    # t.preOrderTraverse(t.root)
    # print(depth(t.root))
    # t.inOrderTraverse(t.root)
    # t.posOrderTraverse(t.root)
    s = Solution()
    print (s.diameterOfBinaryTree(t.root))
