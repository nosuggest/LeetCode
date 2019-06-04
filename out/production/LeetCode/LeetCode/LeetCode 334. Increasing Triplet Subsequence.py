class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        min_val = float("inf")
        max_val = float("inf")
        for num in nums:
            if num < min_val:
                min_val=num
            elif min_val<num and num<max_val:
                max_val=num
            elif num>max_val:
                return True
        return False
            