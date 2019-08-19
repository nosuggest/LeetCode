import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        allstr = list(string.ascii_uppercase)
        first_dict = dict(zip(allstr,range(1,len(allstr)+1)))
        l = len(s)
        res = 0
        for i in range(l):
            res +=first_dict[s[-(i+1)]]*pow(26,i)
        return res
