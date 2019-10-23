#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 11:00 AM
# @Author  : Slade
# @File    : LeetCode347top-k-frequent-elements.py

'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = dict()
        for num in nums:
            c[num] = c.get(num, 0) + 1
        length = len(c)
        ans = list(c.items())

        def min_heap(arr, length, idx):
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < length and arr[smallest][1] > arr[left][1]:
                smallest = left

            if right < length and arr[smallest][1] > arr[right][1]:
                smallest = right

            if idx != smallest:
                arr[idx], arr[smallest] = arr[smallest], arr[idx]
                min_heap(arr, length, smallest)

        k_minheap = ans[:k]

        if k <= length:
            # 对于k:维护规模为k的minheap
            for i in range(k // 2 + 1, -1, -1):
                min_heap(k_minheap, k, i)

            for i in range(k, length):
                # 选择性进堆
                if ans[i][1] > k_minheap[0][1]:
                    k_minheap[0] = ans[i]
                    min_heap(k_minheap, k, 0)

        for i in range(k - 1, 0, -1):
            # 小根堆是从小到大的排列，需要进行位置变更
            k_minheap[i], k_minheap[0] = k_minheap[0], k_minheap[i]
            # 交换后，维护的堆规模-1
            k -= 1
            min_heap(k_minheap, k, 0)
        return [item[0] for item in k_minheap]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3, 4, 4, 4, 4], 3))
