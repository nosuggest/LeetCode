#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/27 12:30 PM
# @Author  : Slade
# @File    : LeetCode33search-in-rotated-sorted-array.py
'''

```
因为是螺旋数组，所以理解2点：
1、对于mid = （left+right）>>1来说，要么左侧要么右侧，必然会有一边是有序的
2、判断target在有序侧还是非有序侧，从而决定是修正有序侧还是简单位移
```

ps:二分用的是index:`while end<=right`
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left_index = 0
        right_index = len(nums) - 1

        # 以坐标进行比较，不进行值比较
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if nums[mid_index] == target:
                return mid_index
            '''
            0　　1　　2　　*4*　　5　　6　　7

            7　　0　　1　　*2*　　4　　5　　6

            6　　7　　0　　*1*　　2　　4　　5

            5　　6　　7　　*0*　　1　　2　　4

            4　　5　　6　　*7*　　0　　1　　2

            2　　4　　5　　*6*　　7　　0　　1

            1　　2　　4　　*5*　　6　　7　　0
            '''
            '''右侧有序，有序则必递增，此时如果target值小于最右侧值的话，mid<target<right'''
            if nums[mid_index] < nums[right_index]:
                if nums[right_index] >= target and target > nums[mid_index]:
                    left_index = mid_index + 1
                # 如果在无序区，则递归左侧的下一轮，只需要把right = mid - 1即可
                else:
                    right_index = mid_index - 1


            # '''mid处的值比目标值大'''
            else:
                '''左侧有序'''
                if nums[left_index] <= target and target < nums[mid_index]:
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1

        return -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 8, 1, 2, 3], 8))
