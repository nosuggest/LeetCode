public class Solution206 {
    public ListNode reverseList(ListNode head) {
        if(head == null||head.next == null){
            return head;
        }

        ListNode reversedList = reverseList(head.next);
        ListNode tmp = head.next;
        tmp.next = head;
        head.next = null;

        return reversedList;
    }

}
