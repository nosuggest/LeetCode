# coding=utf-8

'''
更多解释在java代码注释块中
  a b
0 0 0
1 x 0
2 0 x
3 0 0
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (3*sum(set(nums))-sum(nums))/2