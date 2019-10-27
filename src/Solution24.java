/**
 * Created by slade on 2019/6/7.
 */
public class Solution24 {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

//        2->3->4->5->6
        ListNode tmp = head.next;
//        1->3->4->5->6
        head.next = tmp.next;
//        2->1->3->4->5->6
        tmp.next = head;
//        因为tmp和head已经交换完成，只需要把head.next后面排序好即可，递归调用即可
        head.next = swapPairs(head.next);

        return tmp;
    }

    public ListNode swapPairs1(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
/*
* 考虑三个事情
* 第一：什么是终止条件，当前节点为null或者只剩当前节点
* 第二：要给上一层返回什么结果，上一层需要接收什么数据
* 第三：每层需要做什么事情
* */
        ListNode tmp = head.next;

//        这里是最难理解的，不要尝试去搞清楚这一步中的swapPairs的结果是什么，你只需要知道，swapPairs之后的是两两调换好的链表，把他接在head,next之后即可
        head.next = swapPairs(tmp.next);
        tmp.next = head;
        return tmp;
    }

    public static void main(String[] args) {

        ListNode ln = new ListNode(1);
        ListNode probe = ln;
        for (int i = 2; i < 7; i++) {
            probe.next = new ListNode(i);
            probe = probe.next;
        }
        Solution24 s = new Solution24();
        ListNode a = s.swapPairs(ln);
    }

}

