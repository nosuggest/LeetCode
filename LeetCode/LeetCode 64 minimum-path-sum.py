class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])

        mat = [[0 for i in range(c)] for j in range(r)]

        # 初始化最小点
        mat[0][0] = grid[0][0]

        # 初始化行列
        for i in range(1, r):
            mat[i][0] = sum([l[0] for l in grid][:(i + 1)])
        for i in range(1, c):
            mat[0][i] = sum(grid[0][:(i + 1)])

        for i in range(1, r):
            for j in range(1, c):
                mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + grid[i][j]

        return mat[-1][-1]