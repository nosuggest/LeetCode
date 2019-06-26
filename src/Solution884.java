import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution884 {
    public String[] uncommonFromSentences(String A, String B) {
        String unionSentence = A +" "+ B;
        String[] unionSentenceList = unionSentence.split(" ");
        HashMap<String,Integer> hashMap = new HashMap<>();

        List<String> ans = new ArrayList<>();

        for (String item:unionSentenceList) {
            if (hashMap.containsKey(item)){
                hashMap.put(item,2);
            }else {
                hashMap.put(item,1);
            }
        }

        for (String key:hashMap.keySet()){
            if (hashMap.get(key)==1) {
                ans.add(key);
            }
        }

        return ans.toArray(new String[ans.size()]);
    }

    public static void main(String[] args) {
        Solution884 s = new Solution884();
        String  A = "apple apple";
        String B = "banana";
        System.out.println(Arrays.toString(s.uncommonFromSentences(A,B)));
    }
}
