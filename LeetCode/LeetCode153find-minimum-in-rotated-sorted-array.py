#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 9:13 AM
# @Author  : Slade
# @File    : LeetCode153find-minimum-in-rotated-sorted-array.py


# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
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

            # 右侧有序，当前值有可能就是结果，不能减去
            if nums[right] >= nums[mid]:
                right = mid
            else:
                # 右侧无序，当前值必不是结果，右移
                left = mid + 1
        return nums[left]

if __name__ == '__main__':
    print(Solution().findMin([3, 1, 2]))
