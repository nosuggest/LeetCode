/**
 * Created by slade on 2019/6/11.
 */
public class Solution779 {
    public int kthGrammar(int N, int K) {
        if (N == 1) return 0;
        if (N == 2 && K == 1) return 0;
        if (N == 2 && K == 2) return 1;

        int lastLength = (1 << (N - 1)) / 2;

        if (K <= lastLength) {
            return kthGrammar(N - 1, K);
        } else {
            return 1 - kthGrammar(N - 1, K - lastLength);
        }

    }

    public static void main(String[] args) {
        Solution779 s = new Solution779();
        System.out.println(s.kthGrammar(30, 1));
    }
}
