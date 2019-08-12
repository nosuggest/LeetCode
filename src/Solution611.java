import java.util.Arrays;

/**
 * Created by slade on 2019/8/12.
 */
public class Solution611 {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for(int i = 0;i<nums.length - 2;i++){
            for(int j = i+1;j<nums.length - 1;j++){
                for(int k = j+1;k<nums.length;k++){
                    //提前剪枝
                    if(nums[i] + nums[j] <= nums[k]){
                        break;
                    }
                    result++;
                }
            }
        }
        return result;
    }
}
