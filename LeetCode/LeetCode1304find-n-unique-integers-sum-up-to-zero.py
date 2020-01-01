class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        tmp = list(range(1,(n>>1)+1))
        tmp1 = [-1*i for i in tmp]
        return tmp+tmp1 if n ==(n>>1)*2 else tmp+tmp1+[0]