#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 11:59 AM
# @Author  : Slade
# @File    : LeetCode621task-scheduler.py

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        hashmap = defaultdict()

        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1

        hashmap = sorted(hashmap.items(), key=lambda x: x[1],reverse=True)

        # 理解一下，出现次数最多的那个字母（出现次数-1）x时间窗口及为最小次数，剩余要考虑的是都为最多次数的字母数
        res = (hashmap[0][1] - 1) * (n + 1)
        for item in hashmap:
            if item[1] == hashmap[0][1]:
                res += 1
        return res if res > len(tasks) else len(tasks)

if __name__ == '__main__':
    print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))