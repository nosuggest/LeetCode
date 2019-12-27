#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 3:48 PM
# @Author  : Slade
# @File    : LeetCode713subarray-product-less-than-k.py
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0 or k == 1:
            return 0
        res = 0
        start = 0
        length = len(nums)
        # [10,5,2,6]
        # [0,1,2,3]
        tmp = 1
        for i in range(0, length):
            tmp *= nums[i]
            while tmp >= k:
                tmp /= nums[start]
                start += 1
            # 右区间-左区间+1正好为不重复的个数
            res += i - start + 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
