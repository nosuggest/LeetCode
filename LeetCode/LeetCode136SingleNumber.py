#question: https://leetcode.com/problems/single-number-ii/description/

'''
题目描述：给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。举个例子：
输入: [2,2,1]
输出: 1
'''
reduce(lambda x, y: x ^ y, tarray)