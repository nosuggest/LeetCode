import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/6/26.
 */
public class Solution46 {

    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    List<List<Integer>> ansTmp = new ArrayList<List<Integer>>();

    public List<List<Integer>> permute(int[] nums) {
        getPermute(1, nums, ansTmp);
        return ans;
    }

    void getPermute(int index, int[] nums, List<List<Integer>> ansTmp) {
        // 跳出条件
        if (index > nums.length) {
            ans = ansTmp;
            return;
        }
        // 初始化
        if (index == 1) {
            for (int i = 0; i < nums.length; i++) {
                List tmp = new ArrayList<>();
                tmp.add(nums[i]);
                ansTmp.add(tmp);
            }
        } else {
            // f(n) = f(n-1) + r

            List<List<Integer>> ansTmp1 = new ArrayList<List<Integer>>();
            for (List list : ansTmp) {
                for (int item : nums) {
                    // 排除重复值
                    if (!list.contains(item)) {

                        // 追加新值
                        List lList = new ArrayList<>(list);
                        lList.add(item);
                        ansTmp1.add(lList);

                    }
                }
            }
            ansTmp = ansTmp1;
        }
        getPermute(index + 1, nums, ansTmp);
    }

    public static void main(String[] args) {
        Solution46 s = new Solution46();
        int[] nums = {1, 2, 3};
        System.out.println(s.permute(nums));

    }

}
