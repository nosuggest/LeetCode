#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:16 AM
# @Author  : Slade
# @File    : LeetCode76minimum-window-substring.py
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        # 双指针
        right = left = 0
        # target需求统计
        charCount = dict()
        for i in t:
            charCount[i] = charCount.get(i, 0) + 1
        # 查找阶段
        lookup = {}

        min_len = float("inf")
        result = ""

        while right < len(s):
            lookup[s[right]] = 1 + lookup.get(s[right], 0)
            right += 1
            # 满足条件了
            while all((lookup.get(x, 0) >= charCount.get(x) for x in charCount.keys())):
                if (right - left) < min_len:
                    min_len = right - left
                    result = s[left:right]
                # 左指针右移
                lookup[s[left]] -= 1
                left += 1

        return result


if __name__ == '__main__':
    print(Solution().minWindow("aaxa", "aa"))
