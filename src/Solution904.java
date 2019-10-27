import java.util.ArrayList;
import java.util.HashSet;

/**
 * Created by slade on 2019/8/19.
 */
public class Solution904 {
    public int totalFruit(int[] tree) {
        if (tree.length == 0) {
            return 0;
        }

        int start = 0;
        int ans = 0;
        int tmp = 1;
        ArrayList arr = new ArrayList();
        arr.add(tree[0]);

        for (int i = 1; i < tree.length; i++) {
            System.out.println(arr);
            if (arr.contains(tree[i])) {
                tmp++;
            } else if (arr.size() < 2) {
                tmp++;
                arr.add(tree[i]);
            } else {
                ans = Math.max(ans, tmp);
                tmp = i - start + 1;
                arr.clear();
                arr.add(tree[i]);
                arr.add(tree[i - 1]);
            }
            if (tree[i] != tree[i - 1]) {
                start = i;
            }

        }

        return Math.max(ans, tmp);
    }

    public static void main(String[] args) {
        int[] tree = {1, 0, 1, 4, 1, 4, 1, 2, 3};
        Solution904 s = new Solution904();
        System.out.println(s.totalFruit(tree));
    }
}
