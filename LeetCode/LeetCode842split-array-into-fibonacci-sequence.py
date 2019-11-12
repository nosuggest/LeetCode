#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 11:02 AM
# @Author  : Slade
# @File    : LeetCode842split-array-into-fibonacci-sequence.py

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        # 递归检验子串是否符合要求
        def confirm(sub1, sub2, S, tmp):
            if (not S) and tmp:
                return tmp + [sub1, sub2]
            if S.startswith(str(int(sub1) + int(sub2))):
                return confirm(sub2, str(int(sub1) + int(sub2)), S[len(str(int(sub1) + int(sub2))):], tmp + [sub1])
            else:
                return []

        for i in range(1, (len(S) >> 1) + 1):
            # 两位数以上开头不许为0
            if S[0] == "0" and i > 1:
                break
            tmp = []
            for j in range(1, len(S)):
                # 两位数以上开头不许为0
                if S[i] == "0" and j > 1:
                    break
                # 提前跳出
                if max(i, j) > len(S) - i - j:
                    break

                r = confirm(S[:i], S[i:i + j], S[i + j:], tmp)
                # 范围约束
                if r and int(r[-1]) <= 2147483647:
                    return r
        return []


if __name__ == '__main__':
    print(Solution().splitIntoFibonacci("123456579"))
