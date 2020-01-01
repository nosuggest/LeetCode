public class Solution1304 {
    public int[] sumZero(int n) {
        int[] res = new int[n];
        int temp = n >> 1;

        for (int i = 0; i < temp; i++) {
            res[i] = i + 1;
            res[n - i - 1] = -i - 1;
        }
        if (n != temp * 2) {
            res[temp] = 0;
        }
        return res;
    }
}
