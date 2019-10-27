#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 7:13 PM
# @Author  : Slade
# @File    : LeetCode889construct-binary-tree-from-preorder-and-postorder-traversal.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        if not pre and not post:
            return None

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        split_point = post.index(pre[1])

        root.left = self.constructFromPrePost(pre[1:2 + split_point], post[:split_point + 1])
        root.right = self.constructFromPrePost(pre[2 + split_point:], post[split_point + 1:-1])
        return root


if __name__ == '__main__':
    s = Solution()
    s.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
