public class Solution1004 {
    public int longestOnes(int[] A, int K) {
        int maxLength = -1;
        int length = A.length;
        int left = 0;
        int right = 0;

        while (left < length || right < length) {
            while ((right < length) && (A[right] == 1 || K > 0)) {
                if (A[right] == 1) {
                    ++right;
                } else {
                    ++right;
                    --K;
                }
            }
            maxLength = Math.max(maxLength, right - left);

            if (left < length && A[left] == 1) {
                ++left;
            } else {
                ++left;
                ++K;
            }

        }
        return maxLength;
    }

    public static void main(String[] args) {
        Solution1004 solution1004 = new Solution1004();
        System.out.println(solution1004.longestOnes(new int[]{0, 0, 1, 1, 1, 0, 0}, 0));
    }
}