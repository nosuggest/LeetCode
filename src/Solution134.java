public class Solution134 {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int maxProfit = -1;
        int totalProfit = 0;
        int seat = -1;
        for (int i = gas.length - 1; i > -1; i--) {
            totalProfit += gas[i] - cost[i];
            if (totalProfit > maxProfit) {
                maxProfit = totalProfit;
                seat = i;
            }
        }
        /*保证至少满足gas>cost*/
        if (totalProfit < 0) {
            return -1;
        }
        return seat;
    }

    public static void main(String[] args) {
        System.out.println(new Solution134().canCompleteCircuit(new int[]{3, 3, 4}, new int[]{3, 4, 4}));
    }
}
