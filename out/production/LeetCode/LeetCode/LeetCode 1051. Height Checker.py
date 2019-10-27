class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        return sum([sorted_heights[i] != heights[i] for i in range(len(heights))])