class Solution663 {
    public boolean judgeSquareSum(int c) {
        int start = 0;
        int end = (int) Math.sqrt(c) + 1;
        while (start <= end) {
            if (start * start + end * end == c) {
                return true;
            } else if (start * start + end * end > c) {
                end--;
            } else {
                start++;
            }
        }
        return false;
    }
}