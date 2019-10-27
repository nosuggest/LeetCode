#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 7:50 PM
# @Author  : Slade
# @File    : LeetCode653two-sum-iv-input-is-a-bst.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        def helper(root):
            out = []
            if root:
                out = helper(root.left) + [root.val] + helper(root.right)
            return out

        ans = helper(root)
        return any([(k - ans[item]) in ans[:item] + ans[item + 1:] for item in range(len(ans))])

    def search(self, root, k):
        if not root:
            return None

        if root.val == k:
            return root
        if k < root.val:
            return self.search(root.left, k)
        else:
            return self.search(root.right, k)

    def another_findTarget(self, node, root, k):
        '''
        :param node:
        :param root:必须有个root，因为要从根结点进行搜索，不然会漏
        :param k:
        :return:
        '''
        if not node:
            return None
        target = k - node.val

        flag = self.search(root, target)

        if flag and flag != node:
            return True
        return self.another_findTarget(node.left, root, k) or self.another_findTarget(node.right, root, k)
