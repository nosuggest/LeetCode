#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 2:55 PM
# @Author  : Slade
# @File    : LeetCode297serialize-and-deserialize-binary-tree.py
'''

```
        tmp = data.pop(0)
        if tmp == "null":
            return None
        root = TreeNode(int(tmp))
```
这三行很重要，`data.pop`不断的拿结点去赋值，`if`判断条件用来当数据到最底层时候，跳出此次递归分支，切换到另一个子树上（此处为右子树）

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.ans = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            self.ans.append("null")
            return self.ans
        self.ans.append(str(root.val))
        self.serialize(root.left)
        self.serialize(root.right)
        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 空树
        if len(data) == 1 and data[0] == "null":
            return None
        tmp = data.pop(0)
        if tmp == "null":
            return None
        root = TreeNode(int(tmp))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
