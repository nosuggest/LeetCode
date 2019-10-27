#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 连乘质数和.py
@Author: sladesha
@Date  : 2019/9/16 22:38
@Desc  : 
'''

from collections import defaultdict


def getAns(value):
    dp = defaultdict(int)
    for i in range(2, value + 1):
        if not dp.get(i):
            tmp = 0

            def getPrime(num):
                nonlocal tmp
                nonlocal dp
                if num == 1:
                    return
                for i in range(2, num + 1):
                    if num % i == 0:
                        tmp += dp.get(i, 1)
                        getPrime(int(num / i))
                        break
                if not dp.get(num):
                    dp[num] = tmp

            getPrime(i)

    return sum(dp.values())


import math


def iszhishu(x):
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def get_result(n):
    dic = {}
    rec = []
    for i in range(2, n + 1):
        if iszhishu(i):
            dic[i] = 1
            rec.append(i)
        else:
            for j in rec:#保存所有质数，方便去找质数和
                if i % j == 0:
                    dic[i] = dic[i // j] + 1#i//j必然已经算过
    ans = 0
    for i in range(2, n + 1):
        ans += dic[i]


if __name__ == '__main__':
    print(getAns(6))
