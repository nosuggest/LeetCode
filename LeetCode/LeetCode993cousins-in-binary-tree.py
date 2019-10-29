#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 12:11 AM
# @Author  : Slade
# @File    : LeetCode993cousins-in-binary-tree.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
```python
depth[root.val] = depth[par.val]+1 if par else 0
parent[root.val] = par
```
对于根层，depth\[root.val]=0，parent\[root.val]=None
'''
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        '''本来用的是层次遍历，过于复杂，改为递归'''

        depth = {}
        parent = {}

        def dfs(node, pare):
            if node:
                depth[node.val] = dept[pare.val] + 1 if pare else 0
                pare[node.val] = pare
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)
        return depth[x] == depth[y] and parent[x] != parent[y]
