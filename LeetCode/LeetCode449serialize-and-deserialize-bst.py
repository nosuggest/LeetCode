#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 7:46 PM
# @Author  : Slade
# @File    : LeetCode449serialize-and-deserialize-bst.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preOrderTraverse(root):
            out = []
            if root:
                out += [str(root.val)]
                out += preOrderTraverse(root.left)
                out += preOrderTraverse(root.right)
            return out

        return "|".join(preOrderTraverse(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        def build_tree(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            split_point = inorder.index(preorder[0])
            root.left = build_tree(preorder[1:split_point + 1], inorder[:split_point])
            root.right = build_tree(preorder[split_point + 1:], inorder[split_point + 1:])
            return root

        data = list(map(int, data.split("|")))
        data1 = sorted(data)
        return build_tree(data, data1)

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))