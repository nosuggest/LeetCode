#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 8:42 PM
# @Author  : Slade
# @File    : LeetCode306additive-number.py

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        length = len(num)

        def conform(sub1, sub2, num):
            if not num:
                return True
            sub1, sub2 = sub2, str(int(sub1) + int(sub2))
            return num.startswith(sub2) and conform(sub1, sub2, num[len(sub2):])

        for i in range(1, (length >> 1) + 1):
            # sub1的首位不为0
            if num[0] == "0" and i > 1:
                return False

            sub1 = num[:i]
            for j in range(1, length):
                # i+j>n-i-j
                if max(i, j) > length - i - j:
                    break
                # sub2的首位不为0
                if num[i] == "0" and j > 1:
                    break
                sub2 = num[i:i + j]
                if conform(sub1, sub2, num[i + j:]):
                    return True
        return False

if __name__ == '__main__':
    print(Solution().isAdditiveNumber("199100199"))