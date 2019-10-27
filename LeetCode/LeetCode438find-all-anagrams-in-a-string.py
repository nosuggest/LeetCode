#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 10:15 AM
# @Author  : Slade
# @File    : LeetCode438find-all-anagrams-in-a-string.py

'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
'''


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        if not s:
            return ans

        windows = {}
        targets = {}

        for c in p:
            targets[c] = targets.get(c, 0) + 1

        left, right = 0, 0
        length, limit = len(s), len(p)
        while right < length:
            c = s[right]
            if c not in targets:
                # 之前一致的都失效，全部清零
                windows.clear()
                left = right = right + 1
            else:
                windows[c] = windows.get(c, 0) + 1
                if right - left + 1 == limit:
                    if targets == windows:
                        ans.append(left)
                    windows[s[left]] -= 1
                    left += 1
                right += 1
        return ans