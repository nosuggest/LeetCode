import java.util.Arrays;

/**
 * Created by slade on 2019/8/5.
 */
public class Solution922 {
    public int[] sortArrayByParityII(int[] A) {
        Arrays.sort(A);
        int ans[] = new int[A.length];
        int odd_idx = 1;
        int even_idx = 0;

        for (int i = 0; i <A.length; i++) {
            if (A[i] % 2 == 1) {
                ans[odd_idx] = A[i];
                odd_idx += 2;
            } else {
                ans[even_idx] = A[i];
                even_idx += 2;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution922 s = new Solution922();
        int[] a = {4,2,5,7};
        System.out.println(Arrays.toString(s.sortArrayByParityII(a)));
    }
}
