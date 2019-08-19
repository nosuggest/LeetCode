/**
 * Created by slade on 2019/5/30.
 */
public class solution9 {
    public boolean isPalindrome(int x) {
        boolean tag;
        String s = String.valueOf(x);
        int length = s.length();
        String reverse_s = "";
        for (int i = length - 1; i >= 0; i--) {
            reverse_s = reverse_s + s.charAt(i);
        }
//        System.out.println(reverse_s);
        if (s.equals(reverse_s)) {
            tag = true;
        } else {
            tag = false;
        }

        return tag;
    }

    public static void main(String[] args) {
        solution9 s = new solution9();
        System.out.println(s.isPalindrome(92318));
    }
}
