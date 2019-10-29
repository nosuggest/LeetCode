#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 9:41 AM
# @Author  : Slade
# @File    : LeetCode55jump-game.py
'''
```python
max_dis：上次每次可跳的最远距离
本次是在range中产生的，所以需要减去1，剩下的才是还可供跳跃的长度

nums[idx]：是本次新可跳的距离

比较max_ids-1和nums[idx]得出当前可跳的新最远距离
如果max_ids==0代表可跳的距离额度没有了，return False
```

这题和[distribute-coins-in-binary-tree](LeetCode/LeetCode979distribute-coins-in-binary-tree.py)神似。
'''
class Solution0(object):
    '''
    超时
    '''

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        dp = len(nums) * [False]
        dp[0] = True

        for idx in range(1, len(nums)):
            for j in range(idx, -1, -1):
                if dp[j] and nums[j] + j >= idx:
                    dp[idx] = True
                    break
        return dp[-1]


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        max_dis = 0
        for idx in range(len(nums) - 1):
            '''
            max_dis：上次每次可跳的最远距离
            本次是在range中产生的，所以需要减去1，剩下的才是还可供跳跃的长度

            nums[idx]：是本次新可跳的距离

            比较max_ids-1和nums[idx]得出当前可跳的新最远距离
            如果max_ids==0代表可跳的距离额度没有了，return False
            '''
            max_dis = max(max_dis - 1, nums[idx])
            if max_dis == 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([3, 2, 1, 0, 4]))
