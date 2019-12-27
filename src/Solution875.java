/**
 * Created by slade on 2019/12/27.
 */
public class Solution875 {
    public int minEatingSpeed(int[] piles, int H) {
        if (H == 1) {
            return piles[0];
        }
        int start = 0;
        int end = 0;
        for (int i = 0; i < piles.length; i++) {
            start += piles[i];
            end = Math.max(end, piles[i]);
        }
        start = (start - 1) / H + 1;
        int mid;
        while (start < end) {
            mid = (start + end) >> 1;
            if (!isMatch(piles, H, mid)) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }

    public Boolean isMatch(int[] piles, int H, int key) {
        int tmp = 0;
        for (int i = 0; i < piles.length; i++) {
            tmp += (piles[i] - 1) / key + 1;
        }
        if (tmp <= H) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Solution875 solution875 = new Solution875();
        int[] a = new int[]{3, 6, 7, 11};
        int k = 8;
        System.out.println(solution875.minEatingSpeed(a, k));
    }
}
