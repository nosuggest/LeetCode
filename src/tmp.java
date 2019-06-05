import java.lang.reflect.Array;
import java.util.*;

/**
 * Created by slade on 2019/5/31.
 */


public class tmp {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode next = head.next;
        head.next = swapPairs(next.next);
        next.next = head;
        return next;
    }
    public static void main(String[] args) {
        ListNode a= new ListNode(0);
        ListNode b = a;
        for (int i=1;i<=5;i++){
            b.next = new ListNode(i);
            b = b.next;
        }
        System.out.println(a.val);

        tmp c = new tmp();
        System.out.println(c.swapPairs(a).next.next.next.val);


    }

}



