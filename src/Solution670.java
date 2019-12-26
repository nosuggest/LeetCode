import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

/**
 * Created by slade on 2019/12/26.
 */
public class Solution670 {
    public int maximumSwap(int num) {
        ArrayList<Integer> arrayList = new ArrayList();
        while (num != 0) {
            arrayList.add(num % 10);
            num /= 10;
        }
        Collections.reverse(arrayList);
        ArrayList arrayList1 = new ArrayList(arrayList);
        arrayList1.sort(new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                return (Integer) o1 > (Integer) o2 ? -1 : 1;
            }
        });
        for (int i = 0; i < arrayList.size(); i++) {
            if (arrayList.get(i) != arrayList1.get(i)) {
                int tmp = (int) arrayList1.get(i);
                int idx = arrayList.lastIndexOf(tmp);
                arrayList.set(idx, arrayList.get(i));
                arrayList.set(i, tmp);
                break;
            }
        }
        int res = 0;
        for (int i = 0; i < arrayList.size(); i++) {
            res = 10 * res + arrayList.get(i);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution670 solution670 = new Solution670();
        System.out.println(solution670.maximumSwap(134120));
    }
}
