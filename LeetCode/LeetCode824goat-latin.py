#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode824goat-latin.py.py
@Author: sladesha
@Date  : 2019/8/19 23:21
@Desc  : 
'''


class Solution(object):
    def __init__(self):
        self.key =  ["a","e","i","o","u"]

    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        sl = list(map(self.deal_func,S.split(" ")))
        al = list(range(1,(len(sl)+1)))
        out = []
        for idx in range(len(sl)):
            out.append(sl[idx]+al[idx]*"a")
        return " ".join(out)

    def deal_func(self,word):
        if word[0].lower() in self.key:
            return word+"ma"
        else:
            return word[1:]+word[0]+"ma"