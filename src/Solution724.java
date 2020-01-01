public class Solution724 {
    public int pivotIndex(int[] nums) {
        int temp = 0;
        int s = 0;
        for (int i = 0; i < nums.length; i++) {
            s += nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                temp = 0;
            } else {
                temp += nums[i - 1];
            }
            if (temp == s - nums[i] - temp) {
                return i;
            }
        }
        return -1;
    }
}
