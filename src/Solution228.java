import java.util.ArrayList;
import java.util.List;

public class Solution228 {
    public List<String> summaryRanges(int[] nums) {
        List ans = new ArrayList();
        int length = nums.length;

        int l = 0;
        int r = 0;

        while (r < length) {
            while (r < length - 1 && nums[r] + 1 == nums[r + 1]) {
                ++r;
            }
            if (l != r) {
                ans.add(Integer.toString(nums[l]) + "->" + Integer.toString(nums[r]));
            } else {
                ans.add(Integer.toString(nums[l]));
            }
            ++r;
            l = r;
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution228 solution228 = new Solution228();
        int[] nums = new int[]{0,2,3,4,6,8,9};
        System.out.println(solution228.summaryRanges(nums));
    }
}
