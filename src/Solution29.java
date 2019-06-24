public class Solution29 {
    public int divide(int dividend, int divisor) {
        if (divisor == 0) return 0;
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        boolean label;
        if (dividend * divisor > 0) {
            label = true;
        } else {
            label = false;
        }

        long dividendL = Math.abs((long) dividend);
        long divisorL = Math.abs((long) divisor);

        int result = 0;
        for (int i = 31; i >= 0; i--) {
            if ((dividendL >> i) >= divisorL) {
                result += 1 << i;
                dividendL -= divisorL << i;
            }
        }
        result = label ? result : -result;
        return result;
    }

    public static void main(String[] args) {
        Solution29 s = new Solution29();
        System.out.println(s.divide(214748368,-1));
    }
}
