#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 4:31 PM
# @Author  : Slade
# @File    : LeetCode873length-of-longest-fibonacci-subsequence.py

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashmap, res = {}, 0
        for index, value in enumerate(A):
            hashmap[value] = {}
            for offset in range(index - 1, -1, -1):
                # x有可能不存在于A中，y必然存在
                x = value - A[offset]
                y = A[offset]
                if x >= y:
                    break

                if x in hashmap:
                    hashmap[value][y] = hashmap[y].get(x, 2) + 1
                    res = max(res, hashmap[value][y])
        return res


if __name__ == '__main__':
    print(Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
    # {1: {}, 3: {}, 7: {}, 11: {7: 3}, 12: {11: 3, 7: 3}, 14: {12: 3, 11: 3}, 18: {14: 3, 12: 3, 11: 4}}
    # {1: {}, 3: {}, 7: {}, 11: {}, 12: {11: 3}, 14: {11: 3}, 18: {11: 3}}
