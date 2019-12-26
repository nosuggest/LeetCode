#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 3:28 PM
# @Author  : Slade
# @File    : LeetCode1239maximum-length-of-a-concatenated-string-with-unique-characters.py

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        arr = [s for s in arr if len(s)==len(set(s))]

        def dfs(idx, tmp):
            if idx >= len(arr):
                return len(tmp)

            if not (set(tmp) & set(arr[idx])):
                return max(dfs(idx + 1, tmp + arr[idx]), dfs(idx + 1, tmp))
            else:
                return dfs(idx + 1, tmp)

        return dfs(0, "")


if __name__ == '__main__':
    s = Solution()
    print(s.maxLength(["yy","bkhwmpbiisbldzknpm"]))
