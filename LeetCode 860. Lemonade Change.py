class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        keep = []
        for i in bills:
            if i ==5:
                keep.append(5)
            elif i == 10:
                if 5 in keep:
                    keep.remove(5)
                    keep.append(10)
                else:
                    return False
            else:
                if 10 in keep and 5 in keep:
                    keep.remove(5)
                    keep.remove(10)
                elif keep.count(5)>=3:
                    keep.remove(5)
                    keep.remove(5)
                    keep.remove(5)
                else:
                    return False
        return True
            
        
        