import java.util.ArrayList;
import java.util.List;

public class Solution1018 {
    public List<Boolean> prefixesDivBy5(int[] A) {
        List<Boolean> ans = new ArrayList<>();
        int tmp=0;
        for (int i = 0; i < A.length; i++) {
            if ((tmp+A[i])==0||(tmp+A[i]==5)) {
                ans.add(true);
            }else {
                ans.add(false);
            }
            tmp = tmp + A[i];
            tmp = (tmp*2)%10;
            }
        return ans;
        }

    public static void main(String[] args) {
        Solution1018 s = new Solution1018();
        int[] a = {1,1,1,0,1};
        System.out.println(s.prefixesDivBy5(a));
    }
    }

