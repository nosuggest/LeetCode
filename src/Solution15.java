import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/6/5.
 */
public class Solution15 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        int length = nums.length;
        System.out.println(Arrays.toString(nums));
        for (int i = 0; i < length - 2; i++) {
            if (nums[i] > 0) {
                break;
            }
            // 必须为i-1，更靠前的能含更大的可取范围，比如[-1,-1,0,1,2]，如果跳过第一个则结果只有[-1，0，1]，遗漏了[-1,-1,2]
            if (i != 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // 标记指针，而不是用值
            int first = i + 1;
            int last = length - 1;

            while (first < last) {
                int sum = nums[first] + nums[last] + nums[i];
                if (sum == 0) {
                    ans.add(Arrays.asList(nums[first], nums[last], nums[i]));
                    //缩小范围范围继续查找
                    first++;
                    last--;

                    // 加上first<last的限制，防止越界，依旧是first-1还是first+1和first的问题
                    while (first < last && nums[first - 1] == nums[first]) {
                        first++;
                    }
                    while (first < last && nums[last + 1] == nums[last]) {
                        last--;
                    }
                } else if (sum > 0) {
                    last--;
                } else if (sum < 0) {
                    first++;
                }
            }

        }
        return ans;
    }

    public static void main(String[] args) {
        Solution15 s = new Solution15();
        int[] array = {-2, 0, 1, 1, 2};
        System.out.println(s.threeSum(array));
    }
}
