import java.util.Arrays;

/**
 * Created by slade on 2019/12/19.
 */
class Solution646 {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> {
            if (a[1] != b[1]) {
                return a[1] - b[1];
            } else {
                return a[0] - b[0];
            }
        });
        int start = Integer.MIN_VALUE;
        int ans = 0;
        for (int[] item : pairs
                ) {
            System.out.println(Arrays.toString(item));
            if (item[0] > start) {
                ans += 1;
                start = item[1];
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution646 solution646 = new Solution646();
        int[][] pairs = new int[][]{{-6, 9}, {1, 6}, {8, 10}, {-1, 4}, {-1, 4}, {-6, -2}, {-9, 8}, {-5, 3}, {-0, 3}};
        System.out.println(solution646.findLongestChain(pairs));
    }
}
