class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        
        while not num%2:
            num/=2        
        if num==1:
            return True
        
        while not num%3:
            num/=3
        if num==1:
            return True
        
        while not num%5:
            num/=5
        if num==1:
            return True        
        return False