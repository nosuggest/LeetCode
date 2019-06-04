/**
 * Created by slade on 2019/6/4.
 */


public class Solution21 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode ln1 = new ListNode(0);
        ListNode ln2 = ln1;

        while (l1 !=null && l2!=null){
            if (l1.val<=l2.val){
                ln2.next = l1;
                l1 = l1.next;
            }else {
                ln2.next = l2;
                l2 = l2.next;
            }
            ln2 = ln2.next;
        }
        if (l1==null){
            ln2.next=l2;
        }
        if (l2==null){
            ln2.next=l1;
        }
        return ln1.next;
    }
    }


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}