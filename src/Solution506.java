import sun.font.GlyphLayout;

import java.util.Arrays;
import java.util.HashMap;

public class Solution506 {
    public String[] findRelativeRanks(int[] nums) {
        int[] tmp = new int[nums.length];
        System.arraycopy(nums,0,tmp,0,nums.length);
        String[] ans  = new String[nums.length];
        Arrays.sort(tmp);
        int len;
        len = nums.length;
        HashMap<Integer,Integer> hashmap = new HashMap<>();

        for (int i = 0; i < len; i++) {
            hashmap.put(tmp[i],i+1);
        }
        int i = 0;
        for (int num : nums) {
            if (hashmap.get(num)==len) ans[i] = "Gold Medal";
            if (hashmap.get(num)==len-1) ans[i] = "Silver Medal";
            if (hashmap.get(num)==len-2) ans[i] = "Bronze Medal";
            if (hashmap.get(num)<len-2){
                ans[i]  = Integer.toString(len+1-hashmap.get(num));
            }
            i+=1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution506 s = new Solution506();
        int[] nums = {5, 4, 3, 2, 1};
        System.out.println(Arrays.toString(s.findRelativeRanks(nums)));
    }
}
