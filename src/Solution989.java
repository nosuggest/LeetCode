import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution989 {
    public List<Integer> addToArrayForm(int[] A, int K) {
        int KLen = Integer.toString(K).length();
        String KStr = Integer.toString(K);
        List<Integer> KList = new ArrayList<Integer>();
        for (int i = 0; i < KLen; i++) {
            KList.add( Integer.parseInt(String.valueOf(KStr.charAt(i))));
        }

        List<Integer> ans = new ArrayList<>();

        // 倒叙
        List<Integer> AList = new ArrayList<>();

        for (int i = 0; i < A.length; i++) {
            AList.add(A[i]);
        }

        Collections.reverse(AList);
        Collections.reverse(KList);

        int maxLen = Math.max(AList.size(), KList.size());

        List<Integer> zeroList = new ArrayList<>();
        int diff = Math.abs(AList.size()-KList.size());
        while (diff>0){
            zeroList.add(0);
            diff--;
        }
        if (AList.size()>KList.size()){
            KList.addAll(zeroList);
        }else if (AList.size()<KList.size()){
            AList.addAll(zeroList);
        }
        int nextSet = 0;
        for (int i = 0; i < maxLen; i++) {
            int curSum = KList.get(i)+AList.get(i)+nextSet;
            if (curSum>=10){
                ans.add(curSum%10);
                nextSet = curSum/10;
            }else {
                ans.add(curSum);
                nextSet = 0;
            }
        }
        if (nextSet>0){
            ans.add(nextSet);
        }
        Collections.reverse(ans);
        return ans;
    }

    public static void main(String[] args) {
        Solution989 s = new Solution989();
        int[] A = {0};
        int K= 23;
        System.out.println(s.addToArrayForm(A,K));
    }
}
