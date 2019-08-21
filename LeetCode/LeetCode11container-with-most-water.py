#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 2:00 PM
# @Author  : Slade
# @File    : test12.py
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_size = 0
        while left != right:
            max_size = max(max_size, min(height[left], height[right]) * (right - left))
            if height[left] >= height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
        return max_size


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
