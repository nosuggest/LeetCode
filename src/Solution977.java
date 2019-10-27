import java.util.Arrays;

/**
 * Created by slade on 2019/8/5.
 */
public class Solution977 {
    public int[] sortedSquares(int[] A) {
        for (int i = 0; i < A.length; i++) {
            A[i]*=A[i];
        }
        Arrays.sort(A);
        return A;
    }

    public static void main(String[] args) {
        int[] a = {-4,-1,0,3,10};
        Solution977 s = new Solution977();
        System.out.println(Arrays.toString(s.sortedSquares(a)));
    }
}
