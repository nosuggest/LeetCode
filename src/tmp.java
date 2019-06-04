import java.lang.reflect.Array;
import java.util.*;

/**
 * Created by slade on 2019/5/31.
 */


public class tmp {
    public static void main(String[] args) {

        int[] a = {1, 2, 3, 4, 5};
        int[] b = {10, 10, 12, 13, 14};

        List c = Arrays.asList(a);
        ArrayList d = new ArrayList(c);

        outer:
        for (int aa : a) {
            for (int bb : b) {
                System.out.println(aa);
                System.out.println(bb);
                if (bb == 14){
                    break outer;
                }

            }
        }

    }
}



