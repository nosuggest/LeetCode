class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left = 0
        right = 0
        length = len(A)
        tmp = K
        max_l = -1
        while left < length and right < length:
            if A[right] == 1 or tmp > 0:
                if A[right] == 1:
                    right += 1
                else:
                    right += 1
                    tmp -= 1
                max_l = max(max_l, right - left)
            else:
                if A[left] == 1:
                    left += 1
                else:
                    left += 1
                    tmp += 1
        return max_l


if __name__ == '__main__':
    print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
