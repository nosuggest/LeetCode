#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 9:25 PM
# @Author  : Slade
# @File    : 递增间隔删数.py

def remove_element(input_list):
    idx = 0
    num = 0
    while len(input_list) != 1:
        num += 1  # 1,2,3,4,5
        idx += num  # 1,3,6,10,15...

        if idx >= len(input_list):
            idx = idx % len(input_list)
        input_list.pop(idx)
    print(input_list[0])
