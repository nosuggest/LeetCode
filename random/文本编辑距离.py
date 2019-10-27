#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 4:01 PM
# @Author  : Slade
# @File    : 文本编辑距离.py

def word_edit_distinct(str1, str2):
    length1 = len(str1) + 1
    length2 = len(str2) + 1

    dp = [[i + j for i in range(length1)] for j in range(length2)]

    for i in range(1, length1):
        for j in range(1, length2):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    return dp


if __name__ == '__main__':
    print(word_edit_distinct("intention", "execution"))
