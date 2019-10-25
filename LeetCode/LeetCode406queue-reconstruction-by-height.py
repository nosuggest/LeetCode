#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 9:16 PM
# @Author  : Slade
# @File    : LeetCode406queue-reconstruction-by-height.py

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # x[0]降序，x[1]升序
        people = sorted(people, key=lambda x: [-x[0], x[1]])
        result = []
        for p in people:
            result.insert(p[1], p)

        return result


if __name__ == '__main__':
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
