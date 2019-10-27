import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution18 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);
        int length = nums.length;


        for (int i = 0; i < length - 3; i++) {
            if (i != 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for (int j = i + 1; j < length - 2; j++) {
                if (j != i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                int first = j + 1;
                int last = length - 1;
                while (first < last) {
                    int sum = nums[i] + nums[j] + nums[first] + nums[last];
                    if (sum == target) {
                        ans.add(Arrays.asList(nums[i], nums[j], nums[first], nums[last]));
                        first++;
                        last--;
                        while (nums[first] == nums[first - 1] && first < last) {
                            first++;
                        }
                        while (nums[last] == nums[last + 1] && first < last) {
                            last--;
                        }
                    }
                    if (sum > target) {
                        last--;
                    }
                    if (sum < target) {
                        first++;
                    }
                }
            }
        }



        return ans;

    }

    public static void main(String[] args) {
        Solution18 s = new Solution18();
        int[] array = {-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492};
        int taget = 6189;
        System.out.println(s.fourSum(array, taget));
    }
}
