class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        elif len(nums) == 1:
            return sum(nums)
        elif len(nums) == 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0]= nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2]+nums[0]
        for i in range(3,len(nums)):
            dp[i] = max(dp[i-3],dp[i-2])+nums[i]
        return max(dp)