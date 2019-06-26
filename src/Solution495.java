/**
 * Created by slade on 2019/6/26.
 */
public class Solution495 {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.length==0) return 0;

        int start = timeSeries[0];
        int curSum = 0;
        for (int i = 1; i < timeSeries.length; i++) {
            if (timeSeries[i] - start <= duration - 1) {
                curSum += timeSeries[i] - start;
                start = timeSeries[i];
            } else {
                curSum += duration;
                start = timeSeries[i];
            }
        }
        return curSum+duration;
    }

    public static void main(String[] args) {
        Solution495 s  = new Solution495();
        int[] a = {};
        System.out.println(s.findPoisonedDuration(a,2));
    }
}
