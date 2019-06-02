import java.awt.*;
import java.util.*;
import java.util.List;

/**
 * Created by slade on 2019/5/31.
 */
public class tmp {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

    public static void main(String[] args) {
        tmp s = new tmp();
        int [] val = {0,0,1,1,2,2,3,4};
        System.out.println(s.removeDuplicates(val));
    }
}
