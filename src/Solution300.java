import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/8/14.
 */
public class Solution300 {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return 1;
        int maxValue = 0;
        int[] dp = new int[nums.length];
        dp[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxValue = Math.max(maxValue, dp[i]);
        }
        System.out.println(Arrays.toString(dp));
        return maxValue;
    }


    public static void main(String[] args) {
        Solution300 s = new Solution300();
        int[] arr = {2, 2};
        System.out.println(s.lengthOfLIS(arr));
    }

}



