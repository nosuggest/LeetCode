class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''最后一轮拿的时候剩4，则必输；倒数第二轮拿的时候则剩8必输，数学归纳法'''
        return n%4
    