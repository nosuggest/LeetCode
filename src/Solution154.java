/**
 * Created by slade on 2019/12/31.
 */
public class Solution154 {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) >> 1;
            if (nums[mid] < nums[right]) {
                right = mid;
            } else if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                --right;
            }
        }
        return nums[left];
    }

    public static void main(String[] args) {
        System.out.println(new Solution154().findMin(new int[]{3,1,1,3}));
    }
}
