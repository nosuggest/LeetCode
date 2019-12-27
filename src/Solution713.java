/**
 * Created by slade on 2019/12/27.
 */
public class Solution713 {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k == 0 || k == 1) {
            return 0;
        }
        int start = 0;
        int csum = 1;
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            csum *= nums[i];
            while (csum >= k) {
                csum /= nums[start];
                start++;
            }
            ans += i - start + 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution713 solution713 = new Solution713();
        int[] nums = new int[]{10, 5, 2, 6};
        int k = 100;
        System.out.println(solution713.numSubarrayProductLessThanK(nums, k));
    }
}
