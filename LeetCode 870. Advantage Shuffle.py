class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = []
        A.sort()
        for b in B:
            if A[0]>b or A[-1]<=b:
                ans.append(A[0])
                A.pop(0)
            else:
                i,j = 0,len(A)-1
                # j-1的原因是i和j至少要留一个数
                while i<j-1:
                    mid = int((i+j)/2)
                    if A[mid]>b:
                        j = mid
                    elif A[mid]<=b:
                        i = mid
                ans.append(A[j])
                A.pop(j)
        return ans


class Solution1(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        sortA = sorted(A)

        res = [0] * n

        # 列表的序号排序结果
        idx = sorted(range(n), key=lambda x: B[x])
        sorteB = [B[x] for x in idx]

        bf, af = 0, n - 1
        for a in sortA:
            if a > sorteB[bf]:
                res[idx[bf]] = a
                bf += 1
            else:
                # 如更A中的最小的值不能比B中的最小的值大，则必然会去给B中的最大的值，田忌赛马原则
                res[idx[af]] = a
                af -= 1
        return res

if __name__=="__main__":
    s = Solution()
    print(s.advantageCount([12,24,8,32],[13,25,32,11]))