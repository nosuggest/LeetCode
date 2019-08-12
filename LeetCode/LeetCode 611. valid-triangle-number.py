#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 8:20 AM
# @Author  : Slade
# @File    : test.py
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        ans = 0

        def traceback(idx, tmp):
            nonlocal ans
            if idx == length:
                return
            condition3 = tmp[0] + tmp[1] > nums[idx]

            if condition3:
                ans += 1
                traceback(idx + 1, tmp)
            else:
                return

        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                traceback(j + 1, [nums[i], nums[j]])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber(
        [85, 68, 7, 33, 89, 39, 96, 73, 13, 88, 47, 62, 7, 27, 20, 60, 32, 55, 59, 15, 84, 13, 70, 75, 82, 83, 13, 27,
         93, 97, 10, 48, 70, 96, 27, 29, 83, 50, 99, 50, 73, 79, 74, 2, 65, 44, 84, 13, 91, 4, 66, 40, 42, 13, 6, 76,
         70, 96, 25, 55, 83, 69, 67, 60, 49, 94, 39, 20, 99, 95, 44, 47, 27, 98, 21, 59, 35, 58, 16, 63, 88, 22, 93, 79,
         47, 28, 14, 86, 52, 23, 20, 14, 100, 54, 60, 92, 57, 77, 31, 23]))
