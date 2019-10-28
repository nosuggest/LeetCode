#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 3:23 PM
# @Author  : Slade
# @File    : LeetCode42trapping-rain-water.py
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        water = min(max_left , min_left)-height
        '''
        if not height:
            return 0
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        right_max[0] = height[-1]
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in range(1, length):
            right_max[i] = max(right_max[i - 1], height[length - i - 1])

        right_max = right_max[::-1]

        tmp = 0
        for i in range(0, length):
            tmp += min(left_max[i], right_max[i]) - height[i]
        return tmp

    def trap1(self, height):
        length = len(height)
        stack = []

        tmp = 0
        for i in range(length):

            # 当递减栈出现递增元素，进行出栈
            while stack and height[stack[-1]] < height[i]:
                tmp_val = stack.pop()
                if not stack:
                    break
                # stack[-1]为tmp_val的左侧，height为tmp_val的右侧，
                tmp += (min(height[stack[-1]], height[i]) - height[tmp_val]) * (i - stack[-1] - 1)

            stack.append(i)
        return tmp


if __name__ == '__main__':
    print(Solution().trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
