#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 3:40 PM
# @Author  : Slade
# @File    : test17.py
import math
from collections import defaultdict

'''
题目描述:若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
'''


def isPrime(num):
    ans = []
    if num < 2:
        raise ValueError()
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            ans.append(i)
    if len(ans):
        return False
    return True


def splitData(Lists):
    odds = []
    evens = []
    for item in Lists:
        if item % 2 == 0:
            evens.append(item)
        else:
            odds.append(item)
    return odds, evens


def calculate(odds, evens):
    matched = [0] * len(evens)

    ans = 0
    for i in odds:
        used = [0] * len(evens)
        if find(i, used, matched, evens):
            ans += 1
    return ans


def find(x, used, matched, evens):
    for i in range(len(evens)):
        if isPrime(x + evens[i]) and used[i] == 0:
            used[i] = 1
            if matched[i] == 0 or find(matched[i], used, matched, evens):
                matched[i] = x
                return True
    return False


def get_ans(l):
    al, bl = splitData(l)
    return calculate(al, bl)


if __name__ == '__main__':
    print(get_ans([2, 5, 6, 13]))
