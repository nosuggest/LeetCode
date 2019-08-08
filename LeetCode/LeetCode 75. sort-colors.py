class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first, second, last = 0, 0, len(nums) - 1
        while second <= last:
            if nums[second] == 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
                second += 1
            elif nums[second] == 1:
                second += 1
            else:
                nums[second], nums[last] = nums[last], nums[second]
                last -= 1