import java.util.Arrays;

/**
 * Created by slade on 2019/12/26.
 */
public class Solution541 {
    public String reverseStr(String s, int k) {
        if (s.length() > 2 * k) {
            return reverseSingle(s.substring(0, 2 * k), k) + reverseStr(s.substring(2 * k), k);
        } else {
            return reverseSingle(s, k);
        }

    }

    public String reverseSingle(String s, int k) {
        if (s.length() >= k) {
            String s1 = new StringBuffer(s.substring(0, k)).reverse().toString();
            String s2 = s.substring(k).toString();
            return s1 + s2;
        } else {
            String s1 = new StringBuffer(s).reverse().toString();
            return s1;
        }
    }

    public static void main(String[] args) {
        Solution541 solution541 = new Solution541();
        System.out.println(solution541.reverseStr("abcdefg", 2));
    }
}
