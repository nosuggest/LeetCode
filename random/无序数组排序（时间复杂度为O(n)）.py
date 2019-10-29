#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''问题：给你n个无序的int整型数组arr，并且这些整数的取值范围都在0-20之间，要你在 O(n) 的时间复杂度中把这 n 个数按照从小到大的顺序打印出来。'''
tmp = [0]*21
for i in array:
	tmp[i] +=1
for i in range(4):
    for j in range(tmp[i]):
        print(i)
