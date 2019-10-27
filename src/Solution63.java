import java.util.Arrays;

/**
 * Created by slade on 2019/8/14.
 */
class Solution63 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;


        if (obstacleGrid[0][0] == 1) return 0;

        obstacleGrid[0][0] = 1;

        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i - 1][0] == 1 && obstacleGrid[i][0] == 0) {
                obstacleGrid[i][0] = 1;
            } else {
                obstacleGrid[i][0] = 1;
            }
        }

        for (int i = 1; i < n; i++) {
            if (obstacleGrid[0][i - 1] == 1 && obstacleGrid[0][i] == 0) {
                obstacleGrid[0][i] = 1;
            } else {
                obstacleGrid[0][i] = 0;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    obstacleGrid[i][j] = 0;
                } else {
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j];
                }

            }

        }
        return obstacleGrid[m - 1][n - 1];
    }

    public static void main(String[] args) {
        Solution63 s = new Solution63();
        int[][] mat = {
                {0, 1}
        };
        System.out.println(s.uniquePathsWithObstacles(mat));
    }
}