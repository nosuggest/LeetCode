import java.util.Arrays;

/**
 * Created by slade on 2019/6/25.
 */
public class Solution881 {
    public int numRescueBoats(int[] people, int limit) {
        int ans = 0;
        Arrays.sort(people);
        if (people.length == 1) return 1;
        int first_index = 0;
        int last_index = people.length - 1;
        while (last_index >= first_index) {
//            如果只剩一个人让他走
            if (last_index == first_index) {
                ans += 1;
                break;
            }

//            如果最重的人和最轻的人比limit要重，让最重的让走
            if ((people[last_index] + people[first_index]) > limit) {
                ans += 1;
                last_index -= 1;
            } else {
                ans += 1;
                last_index -= 1;
                first_index += 1;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution881 s = new Solution881();
        int[] people = {3,5,3,4};
        System.out.println(s.numRescueBoats(people,3));
    }
}
