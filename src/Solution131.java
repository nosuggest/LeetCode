import java.util.ArrayList;
import java.util.List;

/**
 * Created by slade on 2019/6/26.
 */
public class Solution131 {
    List<List<String>> ans = new ArrayList<>();

    public List<List<String>> partition(String s) {
        List<String> ansValue = new ArrayList<>();
        if (s == "" || s.length() == 0) {
            return ans;
        }
        subPartition(s, 0, ansValue);
        return ans;
    }

    public void subPartition(String s, int index, List<String> ansValue) {
        if (s.length() == index) {
            ans.add(ansValue);
            return;
        }

        for (int i = index + 1; i <= s.length(); ++i) {
            if (isPalindrome(s.substring(index, i))) {
                ansValue.add(s.substring(index, i));
                //已经用ansValue用的是内存地址，时刻在变，所以要new ArrayList<String>(ansValue)固定值使其不变
                subPartition(s, i, new ArrayList<>(ansValue));

                //因为每次执行subPartition会额外add一个其他元素，当所有结果尝试完成或者不满足要求的时候，需要进行回溯把迭代多少次额外加的元素全部剔除
                ansValue.remove(ansValue.size() - 1);

            }
        }
    }


    public boolean isPalindrome(String s) {
        if (s == "" || s.length() == 0) {
            return false;
        }

        //前缀是否回文
        for (int j = 0; j < s.length() / 2; j++) {
            if (s.charAt(j) != s.charAt(s.length() - j - 1)) {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        String s = "abc";
        Solution131 obj = new Solution131();
        System.out.println(obj.partition(s));
    }
}
