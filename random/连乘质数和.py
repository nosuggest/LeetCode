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


if __name__ == '__main__':
    print(getAns(6))