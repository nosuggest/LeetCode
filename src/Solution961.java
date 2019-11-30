import java.util.HashMap;
import java.util.Map;

/**
 * Created by slade on 2019/11/30.
 */
class Solution961 {
    public int repeatedNTimes(int[] A) {
        int length = A.length >> 1;
        Map hashmap = new HashMap<>();
        for (int item : A) {
            if (hashmap.containsKey(item)) {
                int value = (int) hashmap.get(item);
                if (value + 1 == length) {
                    return item;
                }
                hashmap.put(item, value + 1);
            } else {
                hashmap.put(item, 1);
            }
        }
        return -1;
    }
}
