#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 4:39 PM
# @Author  : Slade
# @File    : LeetCode899orderly-queue.py
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K > 1:
            return ''.join(sorted(S))
        tmp = S
        for i in range(len(S)):
            tmp = min(tmp, S[i:] + S[:i])
        return tmp


if __name__ == '__main__':
    s = Solution()
    print (s.orderlyQueue("cba", 1))
