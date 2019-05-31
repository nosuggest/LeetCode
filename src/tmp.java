import java.awt.*;
import java.util.*;
import java.util.List;

/**
 * Created by slade on 2019/5/31.
 */
public class tmp {
    public static void main(String[] args) {
        Stack s = new Stack();
        for(int i = 0;i<10;i++){
            s.push(i);
        }
        System.out.println(s);
        System.out.println(s.search(9));
    }
}
