#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/5 4:27 PM
# @Author  : Slade
# @File    : 意图相似度.py
    
def word_edit_distince(str1, str2):
    # 构造(len(str1)+1) x (len(str2)+1)的矩阵，其中+1是为了考虑str1或者st2为空的情况
    matrix = [[i + j for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # 注意这边从1开始，所以比target和source的时候需要考虑-1
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            # 上侧，左侧，左上侧
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    return matrix[len(str1)][len(str2)]


class Solution:
    def __init__(self):
        self.s = set()
        self.nums = []

    def dfs(self, st, cur):
        if len(cur) >= 3:
            self.s.add(tuple(cur))
        for i in range(st, len(self.nums), 1):
            if len(cur) > 0 and cur[-1] > self.nums[i]:
                continue
            cur.append(self.nums[i])
            self.dfs(st=i + 1, cur=cur)
            cur.pop()

    def findSubsequences(self, nums):
        self.nums = nums
        self.dfs(st=0, cur=[])
        return [list(a) for a in self.s]


def getCount(diff, l1, l2):
    keep = []
    match = []
    length1 = len(l1)
    length2 = len(l2)

    for d1 in range(diff[0], diff[1] + 1):
        for d2 in range(diff[0], diff[1] + 1):
            for idx1 in range(length1 - d1):
                flag = True
                for idx2 in range(length2 - d2):
                    sentence1 = l1[idx1:idx1 + d1]
                    sentence2 = l2[idx2:idx2 + d2]
                    cutoff = word_edit_distince(sentence1, sentence2)
                    if cutoff <= 1 and flag:
                        keep.append(sentence1)
                        match.append(sentence2)
                        flag = False

    print(keep)
    print(match)
    return len(keep) + len(match)


if __name__ == '__main__':
    l1 = ["wea", "jok", "mus", "sto", "jok", "new", "tax", "tem", "pm2"]
    l2 = ["jok", "mus", "new", "sto", "jok", "jok", "new", "tax"]

    print(getCount([3, 5], l1, l2))
