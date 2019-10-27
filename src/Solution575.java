import java.util.Arrays;
import java.util.HashSet;

/**
 * Created by slade on 2019/8/12.
 */
public class Solution575 {
    public int distributeCandies(int[] candies) {
        HashSet hashSet = new HashSet();
        for (int i = 0; i < candies.length; i++) {
            hashSet.add(candies[i]);
        }
        int length0 = candies.length/2;
        int length1 = hashSet.size();

        if (length0>length1){
            return length1;
        }else {
            return length0;
        }

    }

    public static void main(String[] args) {
        Solution575 s = new Solution575();
        int[] candy = {1,1,2,3};
        System.out.println(s.distributeCandies(candy));
    }
}
