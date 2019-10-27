import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by slade on 2019/6/24.
 */
public class Solution932 {
    public int[] beautifulArray(int N) {

        ArrayList<Integer> tmpOdd = new ArrayList<>();
        ArrayList<Integer> tmpEven = new ArrayList<>();
        ArrayList<Integer> tmp = new ArrayList<>();
        ArrayList<Integer> tmp_remove = new ArrayList<>();
        tmp.addAll(Arrays.asList(2, 1, 4, 3));
        if (N == 1) {
            int[] res = new int[]{1};
            return res;
        }
        if (N == 2) {
            int[] res = new int[]{1, 2};
            return res;
        }
        if (N == 3) {
            int[] res = new int[]{3, 1, 2};
            return res;
        }
        while (tmp.size() < N) {
            for (int item : tmp
                    ) {
                tmpOdd.add(item * 2 - 1);
                tmpEven.add(item * 2);
            }
            tmp.clear();
            tmp.addAll(tmpOdd);
            tmp.addAll(tmpEven);
            tmpOdd.clear();
            tmpEven.clear();
        }
        for (int item : tmp) {
            if (item <= N) {
                tmp_remove.add(item);
            }
        }

        int[] res_out = new int[tmp_remove.size()];
        for (int idx = 0; idx < tmp_remove.size(); idx++) {
            res_out[idx] = tmp_remove.get(idx);
        }
        return res_out;
    }

    public static void main(String[] args) {
        Solution932 s = new Solution932();
        System.out.println(Arrays.toString(s.beautifulArray(10)));
    }
}
