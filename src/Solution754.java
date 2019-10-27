/**
 * Created by slade on 2019/7/12.
 */
public class Solution754 {
    int tmp = 1;
    int sum = 0;

    public int reachNumber(int target) {
        target = Math.abs(target);
        while (true) {
            sum += tmp;
            if (target == sum) return tmp;
            if (sum > target) {
                if ((sum - target) % 2 == 0) {
                    return tmp;
                } else if (tmp % 2 == 1) {
                    return tmp + 2;
                } else {
                    return tmp + 1;
                }
            }
            tmp += 1;

        }
    }

    public static void main(String[] args) {
        Solution754 s = new Solution754();
        System.out.println(s.reachNumber(4));
    }

}

