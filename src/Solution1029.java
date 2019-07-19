import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 * Created by slade on 2019/7/19.
 */
public class Solution1029 {
    public int twoCitySchedCost(int[][] costs) {
        int candidate = costs.length;
        int[] vals = new int[candidate];
        int ans = 0;


        for (int i = 0; i < candidate; i++) {
            // 去A比去B贵的程度
            vals[i] = costs[i][0] - costs[i][1];
            // 全去B花多少钱
            ans += costs[i][1];
        }
        Arrays.sort(vals);
        for (int i = 0; i < candidate/2; i++) {
            ans+=vals[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution1029 s = new Solution1029();
        int[][] val = {{10,20},{30,200},{400,50},{30,20}};
        System.out.println(s.twoCitySchedCost(val));
    }


}
