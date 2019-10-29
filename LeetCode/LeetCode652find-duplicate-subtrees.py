#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 5:15 PM
# @Author  : Slade
# @File    : LeetCode652find-duplicate-subtrees.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
'''
```python
out+=[root.val] +self.findDuplicateSubtrees(root.left)+self.findDuplicateSubtrees(root.right)
# 等价于
out+=[root.val]
out+=self.findDuplicateSubtrees(root.left)
out+=self.findDuplicateSubtrees(root.right)
````

```python
if not root:
    return "null"
```
'''

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        res = []
        hashmap = defaultdict(int)

        def helper(root):
            if not root:
                return "null"

            s = str(root.val) + "," + self.findDuplicateSubtrees(root.left) + "," + self.findDuplicateSubtrees(
                root.right)

            if hashmap.get(s, 0) == 1:
                res.append(root)

            hashmap[s] += 1
            return s

        helper(root)
        return res
