#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 9:43 AM
# @Author  : Slade
# @File    : LeetCode154find-minimum-in-rotated-sorted-array-ii.py

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 当有重复的时候，只能移动一位
                # 若 nums[right] 是唯一最小值：那就不可能满足判断条件 nums[mid] == nums[right]，因为 mid < right（left != right 且 mid = (left + right) // 2 向下取整）
                # 核心在于left在更新会加+1，right不会
                right = right - 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([1, 3, 3]))
