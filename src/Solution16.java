import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Created by slade on 2019/6/5.
 */
public class Solution16 {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int length = nums.length;
        int res = nums[0] + nums[1] + nums[length - 1];

        for (int i = 0; i < length - 2; i++) {
            int first = i + 1;
            int last = length - 1;

            if (i != 0 && nums[i - 1] == nums[i]) {
                continue;
            }

            while (first < last) {
                int cur = nums[first] + nums[last] + nums[i];
                if (target == cur) {
                    return target;
                }
                if (Math.abs(target - cur) < Math.abs(target - res)) {
                    res = cur;
                }

                if ((target - cur) > 0) {
                    first++;

                }
                if ((target - cur) < 0) {
                    last--;
                }

            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] a = {0, 2, 1, -3};
        Solution16 s = new Solution16();
        System.out.println(s.threeSumClosest(a, 1));

    }
}
