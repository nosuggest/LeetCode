public class Solution206 {
    public ListNode reverseList(ListNode head) {
        // 左侧为了放在head为null，右侧为递归跳出条件
        if(head == null||head.next == null){
            return head;
        }
        // 对于1-2-3-4-5来说，当递归执行到4-5-null的时候，进行reverseList(5-null)判断会返回5-null不变，则跳过了改行进行4-5这个处理
        ListNode reversedList = reverseList(head.next);

        // 进行反推，把4-5-null中的4和5之间进行断开，tmp=5-null
        ListNode tmp = head.next;
        // tmp = 5-4-5-nul,此处head还是4-5-null
        tmp.next = head;
        // 把4后断开，tmp即为5-4-null
        head.next = null;
        // 因为是直接在地址上进行修改，所以直接返回即可
        return reversedList;
    }

}
