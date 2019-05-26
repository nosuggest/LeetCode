#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 1:43 PM
# @Author  : Slade
# @File    : 合并区间.py

class Solution():
    def merge(self, data):
        '''
        :param data:[[1,2],[3,4],[3,5]]
        :return: [1,2],[3,5]
        '''
        if not data:
            return data

        # 按照第一个元素进行排序
        data.sort(key=lambda x: x[0])

        last = []
        result = []

        for singleone in data:
            if not last:
                last = singleone
                continue
            # 如果不交
            if singleone[0] > last[1]:
                # 保存上次一的最大边界
                result.append(last)
                last = singleone
            # 如果为子集
            else:
                if singleone[1] <= last[1]:
                    continue
                # 有交集则进行替换
                last = [last[0], singleone[1]]
        result.append(last)
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(obj.merge([[1, 4], [4, 5]]))