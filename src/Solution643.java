/**
 * Created by slade on 2019/6/25.
 */
public class Solution643 {
    public double findMaxAverage(int[] nums, int k) {
        int sumAns = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length - (k - 1); i++) {
            int tmpAns = 0;
            for (int j = i; j < i + k; j++) {
                tmpAns += nums[j];
            }

            if (tmpAns > sumAns) sumAns = tmpAns;
        }
        return sumAns / (k*1.0);
    }

    public static void main(String[] args) {
        Solution643 s = new Solution643();
        int[] nums = {1, 12, -5, -6, 50, 3};
        System.out.println(s.findMaxAverage(nums, 4));
    }
}
