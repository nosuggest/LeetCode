/**
 * Created by slade on 2019/8/14.
 */
public class Solution122 {
    public int maxProfit(int[] prices) {
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += prices[i] - prices[i - 1];
            }
        }

        return profit;
    }

    public static void main(String[] args) {
        Solution122 s = new Solution122();
        int[] arr = {7, 6, 4, 3, 1};
        System.out.println(s.maxProfit(arr));
    }
}
