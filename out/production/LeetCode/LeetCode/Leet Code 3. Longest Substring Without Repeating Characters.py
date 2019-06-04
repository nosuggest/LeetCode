#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:20 AM
# @Author  : Slade
# @File    : Leet Code 3. Longest Substring Without Repeating Characters.py

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_num = 0
        defult_dict = {}
        ans = []
        idx = 0
        for letter in s:
            if letter not in ans:
                ans.append(letter)
                defult_dict[letter]=idx
                idx +=1
            else:
                idx = defult_dict[letter]
                ans = ans[idx+1:]+[letter]
                idx = len(ans)
                defult_dict = dict(zip(ans,range(idx)))
            max_num = max(max_num,len(ans))
        return max_num



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))