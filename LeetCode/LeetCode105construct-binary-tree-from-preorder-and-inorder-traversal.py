#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 9:27 AM
# @Author  : Slade
# @File    : LeetCode105construct-binary-tree-from-preorder-and-inorder-traversal.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
需要注意的点：
1. preOrderTraver中的第一个元素必然是根结点，第二个元素开始为左右子树结点
2. inOrderTraver中的找到preOrderTraver中的第一个元素的位置中左侧必然是左子树，右侧必然是右子树
3. **2中找到的左子树长度其实就是list中切点index，且左子树不论在preOrderTraver还是在inOrderTraver中长度必然一致**
4. **preOrderTraver是先遍历左子树再遍历右子树的，所以preOrderTraver[1:3中的长度+1]即为左子树下次递归中的preOrderTraver**
'''

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        split_point = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:split_point + 1], inorder[:split_point])
        root.right = self.buildTree(preorder[split_point + 1:], inorder[split_point + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([1, 2], [1, 2])
