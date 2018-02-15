/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2, int carry){
        if(l1 == null && l2 == null && carry == 0){
            return null;
        }
        int value = carry;
        ListNode res = new ListNode(0);
        if(l1!=null){
            value += l1.val;
        }
        if(l2!=null){
            value+= l2.val;
        }
        res.val = value%10;
        if(l1 != null || l2 != null){
            ListNode add = addTwoNumbers(l1 == null? null: l1.next, l2 == null ? null : l2.next, value >=10 ? 1:0 );
            res.next = add;
        }

        return res;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbers(l1, l2, 0);
    }
}