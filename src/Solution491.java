import java.util.*;

/**
 * Created by slade on 2019/6/28.
 */
public class Solution491 {
    List<List<Integer>> ans = new ArrayList<>();
    List<Integer> init = new ArrayList<>();
    HashSet<String> hashSet = new HashSet<>();

    public List<List<Integer>> findSubsequences(int[] nums) {
        Subsquences(nums, init);
        return ans;
    }

    void Subsquences(int[] nums, List<Integer> tmp) {
        if (tmp.size() > 1 && !hashSet.contains(tmp.toString())) {
            ans.add(tmp);
            hashSet.add(tmp.toString());
        }
        for (int i = 0; i < nums.length; i++) {

            if (tmp.size() == 0 || tmp.get(tmp.size() - 1) <= nums[i]) {
                int[] nextNums = Arrays.copyOfRange(nums, i + 1, nums.length);
                List<Integer> nextTmp = new ArrayList<>(tmp);
                nextTmp.add(nums[i]);
                Subsquences(nextNums, nextTmp);
            }
        }
    }

    public static void main(String[] args) {
        Solution491 s = new Solution491();
        int[] nums = {4, 6, 7, 7};
        System.out.println(s.findSubsequences(nums));
    }

}
