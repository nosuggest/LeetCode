class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        dp = [[0]*i for i in range(1,row+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1,row):
            dp[i][0] = dp[i-1][0]+triangle[i][0]

        for j in range(1,row):
            dp[j][-1] = dp[j - 1][-1]+triangle[j][-1]

        for k in range(2,row):
            print(k)
            for z in range(1,k):
                dp[k][z] = min((dp[k-1][z]+triangle[k][z]),(dp[k-1][z-1]+triangle[k][z]))

        return min(dp[-1])