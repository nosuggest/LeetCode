#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 7:49 PM
# @Author  : Slade
# @File    : 字典序.py

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        基础概念，这个方法解题会超时，但是是为了熟悉字典序概念
        """
        n = list(range(1, n + 1))

        def dict_order(n):
            for i in range(len(n) - 2, -1, -1):
                if n[i - 1] < n[i + 1]:
                    break
            else:
                return n
            print(i)
            for j in range(len(n) - 1, i - 1, -1):
                if n[j] > n[i - 1]:
                    break

            n[i - 1], n[j] = n[j], n[i - 1]
            return n[:i] + n[i:][::-1]

        last_time = n
        while last_time != dict_order(n):
            last_time = dict_order(n)
        return n


class Solution1(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
            起始我们放置[1，9]
    	|放置1，我们放置[10，19]，递归
    	|	放置[10,19]
    	|		|首先放置10,然后放置[100, 109]，递归
    	|		|	放置[100,109]
    	|		|		|放置100，然后放置[1000,1009]，递归
    	|		|		|放置101，然后放置[1010,1019]，递归
    	|		|		|.
    	|		|		|放置109，然后放置[1090,1099]，递归
    	|		|
    	|		|然后放置11,再放置[110, 119]，递归
    	|		|.
    	|		|最后放置19，再放置[190, 199]，递归
    	|接着放置2，然后放置[20, 29]，递归
    	|接着放置3，然后放置[30, 39]，递归
    	|接着放置4，然后放置[40, 49]，递归
    	|.
    	|接着放置9，然后放置[90, 99]，递归
        """
        res=[];num=1
        res.append(num)
        for i in range(1,n):
            if num * 10 <= n:
                num*=10
            else:
                while num % 10 == 9 or num == n:
                    num /= 10
                    num=int(num)
                num+=1
            res.append(num)
        return res


class Solution2(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        n = list(range(1, n + 1))
        '''Python 中sorted是内建函数(BIF),而sort()是列表类型的内建函数list.sort()'''
        return list(map(int,sorted(map(str,n))))