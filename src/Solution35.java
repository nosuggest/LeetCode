import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/6/3.
 */
public class Solution35 {
    public int searchInsert(int[] nums, int target) {
        int idx=0;

        if (nums[nums.length - 1] < target) {
            return nums.length;
        }

        if (nums[0] > target) {
            return  0;
        }

        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
            if (nums[i] == target) {
                idx = i;
            } else if (target > nums[i] && target < nums[i + 1]) {
                idx = i+1;

            }
        }
        return idx;

    }

    public static void main(String[] args) {
        Solution35 s = new Solution35();
        int[] a = {1, 2, 4, 5};
        int b = 3;
        System.out.println(s.searchInsert(a, b));
    }


}
