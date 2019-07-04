import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by slade on 2019/6/28.
 */
public class Solution371 {
    public int getSum(int a, int b) {
        if (b == 0) return a;
        int sum, carry;
        sum = a ^ b;
        carry = (a & b) << 1;
        return getSum(sum, carry);
    }

    public static void main(String[] args) {
        Solution371 s = new Solution371();
        int a = 0;
        int b = 1;
        System.out.println(s.getSum(a, b));
    }
}
