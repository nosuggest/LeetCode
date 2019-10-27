/**
 * Created by slade on 2019/8/14.
 */
public class Solution121 {
    public int maxProfit(int[] prices) {
        int minprofit = Integer.MAX_VALUE;
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            minprofit = Math.min(minprofit, prices[i]);
            profit = Math.max(profit, prices[i] - minprofit);
        }
        return profit;
    }

    public static void main(String[] args) {
        Solution121 s = new Solution121();
        int[] prices = {7,6,4,3,1};
        System.out.println(s.maxProfit(prices));
    }
}
