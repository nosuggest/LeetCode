#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode30substring-with-concatenation-of-all-words.py
@Author: sladesha
@Date  : 2019/11/16 18:59
@Desc  : 
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        single_length = len(words[0])
        total_times = len(words)
        total_length = total_times * single_length
        from collections import Counter
        match_dict = Counter(words)
        ans = []
        for i in range(len(s) - total_length + 1):
            tmp = s[i:i + total_length]
            single_tmp = []
            for j in range(0, total_length, single_length):
                single_tmp.append(tmp[j:j + single_length])
            if Counter(single_tmp) == match_dict:
                ans.append(i)
        return ans

if __name__ == '__main__':
    print (Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))