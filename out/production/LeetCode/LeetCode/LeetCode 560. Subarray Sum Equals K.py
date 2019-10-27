#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:23 AM
# @Author  : Slade
# @File    : 560. 和为K的子数组.py
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt, cur_sum = 0, 0
        # 占位0，得到只有一个元素的值结果
        default_dict = {0: 1}
        # default_dict = {}
        for num in nums:
            cur_sum += num
            if cur_sum - k in default_dict:
                cnt += default_dict[cur_sum - k]
            if cur_sum in default_dict:
                default_dict[cur_sum] += 1
            else:
                default_dict[cur_sum] = 1
        return cnt


'''
if cur_sum - k:
-2
{}
-1
{0: 1}
0
{0: 1, 1: 1}
1
{0: 1, 1: 1, 2: 1}


if k - cur_sum:
2
{}
1
{0: 1}
0
{0: 1, 1: 1}
-1
{0: 1, 1: 1, 2: 1}

主要原因是cur_sum - before_sum = k ,所以是cur_sum - k in dict

'''

if __name__ == "__main__":
    nums = [1, 1, 1]
    s = Solution()
    print(s.subarraySum(nums=nums, k=2))
