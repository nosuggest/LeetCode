class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        c1 = len(candies)/2
        c2=len(set(candies))
        if c2>c1:
            return c1
        else:
            return c2