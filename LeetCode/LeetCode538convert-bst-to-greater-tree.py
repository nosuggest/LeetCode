#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 12:08 AM
# @Author  : Slade
# @File    : LeetCode538convert-bst-to-greater-tree.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.add = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        _ = self.convertBST(root.right)
        root.val += self.add
        self.add = root.val
        _ = self.convertBST(root.left)
        return root
'''

```
1、先遍历到右树的根树，然后把根树的value赋值给add
2、更新此树对应的父结点，并更新父结点对应的value = value+add
3、同时再更新add，把父结点的值也更新到add上
4、再更新父结点的左子树的value结点
5、这样一次更新便完成了
```
'''