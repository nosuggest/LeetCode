public class Solution27 {
    public int removeElement(int[] nums, int val) {
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i]!=val){
                nums[j] = nums[i];
                j++;
            }
        }
    return j;
    }

    public static void main(String[] args) {
        Solution27 s = new Solution27();
        int[] n = {3,1,2,3};
        int v = 3;
        System.out.println(s.removeElement(n,v));
    }
}
