# coding=utf-8

class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        if N==2:
            return [1,2]
        if N==3:
            return [2,1,3]
        res = [2,1,4,3]
        while len(res) < N:
            res1 = list(x*2 for x in res)
            res2 = list(x*2-1 for x in res)
            res = res2+res1

        return list(x for x in res if x in range(N+1))