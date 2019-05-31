import java.util.ArrayList;
import java.util.List;

/**
 * Created by slade on 2019/5/31.
 */
public class Solution14 {
    public String longestCommonPrefix(String[] strs) {
//        待存储
        StringBuffer ans = new StringBuffer("");

        int cnt = 0;

//        快速入口
        if (strs.length <= 0 || strs == null) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }


        int minLength = strs[0].length();

        for (String word : strs) {
            if (word.length() < minLength) {
                minLength = word.length();
            }

        }

        boolean tag = true;
        for (int i = 0; i < minLength; i++) {//词长遍历
            for (int j = 1; j < strs.length; j++) {//词遍历
                if (strs[0].charAt(i) != strs[j].charAt(i)) {
                    tag = false;
                    break;
                }
            }
            if (tag) {
                ans.append(strs[0].charAt(i));
            }

        }
        return ans.toString();
    }

    public static void main(String[] args) {
        Solution14 s = new Solution14();
        String[] strs = {"fog", "flow", "flight"};
        System.out.println(s.longestCommonPrefix(strs));
    }
}
