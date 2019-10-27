import com.sun.deploy.util.StringUtils;

import java.util.Stack;

/**
 * Created by slade on 2019/6/26.
 */
public class Solution1047 {
    public String removeDuplicates(String S) {
        Stack<Character> tmp = new Stack<>();
        for (int i = 0; i < S.length(); i++) {
            if (tmp.empty()){
                tmp.push(S.charAt(i));
                continue;
            }
            if (S.charAt(i)!=tmp.peek()){
                tmp.push(S.charAt(i));
            }else {
                tmp.pop();
            }
        }
        /* 数据的展示可以继续优化 */
        StringBuilder str = new StringBuilder();
        for (Character c : tmp) {
            str.append(c);
        }
        return str.toString();
    }

    public static void main(String[] args) {
        Solution1047 s = new Solution1047();
        String ss = "abbaca";
        System.out.println(s.removeDuplicates(ss));
    }
}
