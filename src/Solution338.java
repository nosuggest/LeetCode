import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by slade on 2019/6/25.
 */
public class Solution338 {
    public int[] countBits(int num) {
        int[] ans = new int[num+1];
        ans[0] = 0;
        for (int i =0;i<=num;i++){
            if (i%2==1){
                ans[i] = ans[i-1]+1;
            }else {
                ans[i] = ans[i/2];
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution338 s = new Solution338();
        System.out.println(Arrays.toString(s.countBits(5)));
    }
}
