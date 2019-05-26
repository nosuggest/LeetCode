class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        for k,v in enumerate(nums):            
            if v in dt:
                return [k,dt[v]]
            dt.update({target-v:k})