import java.util.HashMap;
import java.util.Map;

/**
 * Created by slade on 2019/12/26.
 */
public class Solution485 {
    public int findMaxConsecutiveOnes(int[] nums) {
        int now = 0;
        int max = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                max = Math.max(max, now);
                now = 0;
            } else {
                now++;
            }
        }
        return Math.max(max, now);
    }

    public static void main(String[] args) {
        Solution485 solution485 = new Solution485();
        System.out.println(solution485.findMaxConsecutiveOnes(new int[]{1, 1, 0, 1, 1, 1}));
    }
}
