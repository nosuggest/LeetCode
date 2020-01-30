import java.util.*;

/**
 * Created by slade on 2020/1/30.
 */
public class Solution983 {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[366];
        Set<Integer> hashset = new HashSet<Integer>();

        for (int day : days
                ) {
            hashset.add(day);
        }

        for (int i = 1; i < 366; i++) {
            if (hashset.contains(i)) {
                int tmp1 = Integer.MAX_VALUE;
                int tmp2 = Integer.MAX_VALUE;
                int tmp3 = Integer.MAX_VALUE;
                if (i - 1 >= 0) {
                    tmp1 = dp[i - 1] + costs[0];
                } else {
                    tmp1 = costs[0];
                }
                if (i - 7 >= 0) {
                    tmp2 = dp[i - 7] + costs[1];
                } else {
                    tmp2 = costs[1];
                }
                if (i - 30 >= 0) {
                    tmp3 = dp[i - 30] + costs[2];
                } else {
                    tmp3 = costs[2];
                }
                dp[i] = Math.min(Math.min(tmp1, tmp2), tmp3);
            } else {
                dp[i] = dp[i - 1];
            }
        }
        return dp[365];
    }

    public static void main(String[] args) {
        Solution983 solution983 = new Solution983();
        System.out.println(solution983.mincostTickets(new int[]{1,2,3,4,5,6,7,8,9,10,30,31}, new int[]{2, 7, 15}));
    }
}
