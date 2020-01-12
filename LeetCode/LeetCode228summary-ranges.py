#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : LeetCode228summary-ranges.py
@Author: sladesha
@Date  : 2020/1/12 14:17
@Desc  : 
'''


# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
# 示例 1:
#
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
# 示例 2:
#
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(float("inf"))
        ans = []
        tmp = []
        for i in range(len(nums) - 1):
            if len(tmp) == 2:
                tmp.pop()
            tmp.append(str(nums[i]))
            if nums[i + 1] != nums[i] + 1:
                ans.append("->".join(tmp))
                tmp = []
        return ans


if __name__ == '__main__':
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))
