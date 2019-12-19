#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 9:11 AM
# @Author  : Slade
# @File    : LeetCode646maximum-length-of-pair-chain.py
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs=sorted(pairs,key=lambda x:x[1],reverse=False)
        print(pairs)
        start=pairs[0][1]
        cnt = 1
        for k,v in pairs[1:]:
            if start<k:
                cnt+=1
                start = v
        return cnt

if __name__ == '__main__':
    print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))