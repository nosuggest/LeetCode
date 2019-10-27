class Solution(object):
    def __init__(self):
        self.S = None
    def get_index(self,x):
        if x in self.S:
            return self.S.index(x)
        return -1 
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        self.S = S

        return ''.join(sorted(T,key=lambda x :self.get_index(x)))