/**
 * Created by slade on 2019/7/12.
 */
public class Solution747 {
    public int dominantIndex(int[] nums) {
        int idx = -1;
        if (nums.length == 1) return 0;
        int maxValue = -1;
        int secondValue = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= maxValue) {
                secondValue = maxValue;
                maxValue = nums[i];
                idx = i;
            } else if (nums[i] > secondValue) {
                secondValue = nums[i];
            }
        }
        return maxValue >= secondValue * 2 ? idx : -1;
    }

    public static void main(String[] args) {
        Solution747 s = new Solution747();
        int[] n = {0,0,0,1};
        System.out.println(s.dominantIndex(n));
    }
}
