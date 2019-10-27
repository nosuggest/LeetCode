#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 9:41 AM
# @Author  : Slade
# @File    : 花匠摆花.py

'''
摆红花和白花，连续白花的数目为k的整数倍（可以为0），问总共多少种方法。

输入总共的花的数目区间，如[1,3]表示花数目可以为1、2、3

输入：t组测试用例：

1
2
3
4
5
第一行 t,k

接下来t行区间值

输出：t行 对应每行的方案数
结果对1e9+7取余数

样例：

1
2
3
4
3 2
1 3
2 3
4 4
输出：

1
2
3
6
5
5
解释：

1
2
3
4
5
6
7
8
9
10
k = 2 连续白花个数为0，2，4...
当花的个数为1，2，3，4时，对应的情况为（设a为红花 b为白花）：
1 a 1种
2 aa bb 2种
3 aaa abb bba 3种
4 aaaa bbaa abba aabb bbbb 5种
因此:
[1,3] 1+2+3 = 6
[2,3] 2+3 =5
[4,4] 5
'''


def get_result(size, k):
    dp = 100001 * [0]
    dp[0] = 1
    for i in range(1, 100001):
        '''
        为什么状态转移这么写？把递归的前几步写出来，比如k=2的时候：
        step0: null
        step1：红
        step2：红红，白白
        step3：红红红，白白红，红白白
        step4：红红红红，白白红红，红白白红，红红白白，白白白白
        ...

        以step4举例：分别由step2后每一个加上"白白"+step3后每一个加上"红"即可
        '''
        tmp = dp[i - k] if i >= k else 0
        dp[i] = dp[i - 1] + tmp
    return sum(dp[size[0]:size[1] + 1])


if __name__ == '__main__':
    print(get_result([4, 4], 2))
