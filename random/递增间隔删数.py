#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 9:25 PM
# @Author  : Slade
# @File    : 递增间隔删数.py
'''
有数组A，每个元素存放相应的下标,即A[i]=i，要求按照1,2,3,...的规律删除数组中的元素,第一次间隔1个数，第二次间隔2个数,依次类推，到末尾时循环至开头继续进行,求最后一个被删掉的数的原始下标位置

以上两条都是属于环问题，更多讲解来自：[约瑟夫环问题整理](http://www.shataowei.com/2019/10/20/约瑟夫环问题整理/)
'''
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
