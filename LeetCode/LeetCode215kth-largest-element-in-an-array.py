#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 5:04 PM
# @Author  : Slade
# @File    : LeetCode215kth-largest-element-in-an-array.py

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def min_heap(nums, length, idx):
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < length and nums[left] < nums[smallest]:
                smallest = left
            if right < length and nums[right] < nums[smallest]:
                smallest = right
            if smallest != idx:
                nums[smallest], nums[idx] = nums[idx], nums[smallest]
                min_heap(nums, length, smallest)

        k_min = nums[:k]

        for i in range(k, -1, -1):
            min_heap(k_min, k, i)

        length = len(nums)
        for i in range(k , length):
            if nums[i] > k_min[0]:
                k_min[0] = nums[i]
                # 只要保证小根堆的顶值最小即可
                min_heap(k_min, k, 0)
        return k_min[0]


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
