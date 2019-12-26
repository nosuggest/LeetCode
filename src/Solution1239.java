import java.util.ArrayList;
import java.util.List;

/**
 * Created by slade on 2019/12/26.
 */
public class Solution1239 {
    public int maxLength(List<String> arr) {
        return dfs(0, "", arr);
    }

    public int dfs(int idx, String tmp, List<String> arr) {
        if (idx >= arr.size()) {
            return tmp.length();
        }

        String s = arr.get(idx);

        if (isNotDuplicate(s) && !isCross(tmp, s)) {
            return Math.max(dfs(idx + 1, tmp + s, arr), dfs(idx + 1, tmp, arr));
        } else {
            return dfs(idx + 1, tmp, arr);
        }
    }

    public Boolean isNotDuplicate(String s) {
        for (int i = 0; i < s.length(); i++) {
            char charWord = s.charAt(i);
            int fristPosition = s.indexOf(charWord);
            int lastPosition = s.lastIndexOf(charWord);
            if (fristPosition != lastPosition) {
                return false;
            }
        }
        return true;
    }

    public Boolean isCross(String s1, String s2) {
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    return true;
                }
            }
        }
        return false;
    }


    public static void main(String[] args) {
        Solution1239 solution1239 = new Solution1239();
        ArrayList arrayList = new ArrayList();
        arrayList.add("abcdefghijklmnopqrstuvwxyz");

        System.out.println(solution1239.maxLength(arrayList));
    }
}
