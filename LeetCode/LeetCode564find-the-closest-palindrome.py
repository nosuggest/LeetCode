#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode564find-the-closest-palindrome.py
@Author: sladesha
@Date  : 2019/11/16 13:39
@Desc  : 
'''


# class Solution(object):
#     '''
#     超时
#     '''
#     def nearestPalindromic(self, n):
#         """
#         :type n: str
#         :rtype: str
#         """
#         def is_palindrome(N):
#             return str(N) == str(N)[::-1]
#
#         left = int(n)-1
#         right = int(n)+1
#         while True:
#             if is_palindrome(left):
#                 return str(left)
#             left -=1
#             if is_palindrome(right):
#                 return str(right)
#             right +=1

class Solution(object):
    def nearestPalindromic(self, n):
        """
        参考 @hill141592 的结论,代码比较简洁
        如果n 的前半部分是整数N，那么它的解一定是以下三者之一:
            1. N-1 和 N-1的回文组成的数字。
            2. N 和 N的回文组成的数字
            3. N+1 和 N+1 的回文组成的数字

        :param n:
        :return:
        """
        # 处理特殊情况
        if len(n) == 1:
            return str(int(n) - 1)
        if n in ["10", "11"]:
            return "9"

        mid = len(n) // 2
        # 参照的部分记为part, 需要对称的长度记为mid
        if len(n) % 2 == 0:
            part = n[:mid]
        else:
            part = n[:mid + 1]

        candidate = []
        # 对参照部分-1,0,+1; 然后补成对称
        for i in range(-1, 2):
            p = str(int(part) - i)

            # 处理 12-19的特殊情况, 该情况下-1的不需要考虑, 因为11是最优
            if p == '0':
                continue
            c = p[:mid]  # 找到需要对称的部分
            c = p + c[::-1]  # 翻转成对称

            # 处理(1000,100000,...)的特殊情况, 该情况下 10x->9x, 补成对称后会少一位
            if len(n) - len(c) > 1:
                c = c + c[0]
            candidate.append(c)

        candidate = [int(c) for c in candidate if c != n]  # 去掉自身
        # 选择最优解
        gap = abs(candidate[0] - int(n))
        res = candidate[0]
        for c in candidate[1:]:
            g = abs(c - int(n))
            if g < gap:
                res = c
                gap = g
            elif g == gap:
                if c < res:
                    res = c
        return str(res)