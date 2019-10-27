/**
 * Created by slade on 2019/9/3.
 */
public class Solution279 {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i < dp.length; i++) {
            dp[i] = i;
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution279 s = new Solution279();
        for (int i = 0; i < 13; i++) {
            System.out.println(i);
            System.out.println(s.numSquares(i));
            System.out.println("-----------");
        }
    }
}
