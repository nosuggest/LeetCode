#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 10:18 AM
# @Author  : Slade
# @File    : LeetCode95unique-binary-search-trees-ii.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def get_tree(start, end):
            ans = []
            if start > end:
                ans.append(None)
                return ans

            if start == end:
                ans.append(TreeNode(start))
                return ans

            for i in range(start, end + 1):
                left = get_tree(start, i - 1)
                right = get_tree(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        return get_tree(1, n)

if __name__ == '__main__':
    s = Solution()
    print (s.generateTrees(0))