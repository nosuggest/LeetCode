import java.util.Arrays;

/**
 * Created by slade on 2019/8/14.
 */
public class Solution88 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1_idx = m - 1;
        int nums2_idx = n - 1;
        for (int i = m + n - 1; i > -1; i--) {
            if (nums1_idx >= 0 && nums2_idx >= 0) {
                if (nums1[nums1_idx] > nums2[nums2_idx]) {
                    nums1[i] = nums1[nums1_idx];
                    nums1_idx--;
                } else {
                    nums1[i] = nums2[nums2_idx];
                    nums2_idx--;
                }
            } else if (nums2_idx >= 0) {
                nums1[i] = nums2[nums2_idx];
                nums2_idx--;
            }
        }
    }

    public static void main(String[] args) {
        Solution88 s = new Solution88();
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int m = 3;
        int[] nums2 = {2, 5, 6};
        int n = 3;
        s.merge(nums1, m, nums2, n);
        System.out.println(Arrays.toString(nums1));
    }
}
