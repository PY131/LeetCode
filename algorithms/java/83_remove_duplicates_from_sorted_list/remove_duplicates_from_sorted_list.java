import list.singly_linked_list;
import list.singly_linked_list.ListNode;

/**
 * 
 * @author Peng
 *
 */
public class remove_duplicates_from_sorted_list {

    /**
     * Solution 1: just compare one by one;
     */
    public static class Solution1 {
        public ListNode deleteDuplicates(ListNode head) {
            if(head == null || head.next == null) return head;
            
            ListNode tmp = head;
            while(tmp.next != null){
                if(tmp.val == tmp.next.val) tmp.next = tmp.next.next;
                else tmp = tmp.next;
            }
            
            return head;
        }
    }
    
    /**
     * Solution 2: using recursion to delete duplicates
     */
    public static class Solution2 {
        public ListNode deleteDuplicates(ListNode head) {
            if(head == null || head.next == null) return head;
            
            head.next = deleteDuplicates(head.next);
            return head.val == head.next.val ? head.next : head;
        }
    }
    
    public static void main(String[] args) {
        singly_linked_list<Integer> list = new singly_linked_list<Integer>();
    
        int [] nums = {1,1,2,3};
        for(int i = 0; i < nums.length; i++){
            list.addNode(nums[i]);
        }
        
        Solution1 s1 = new Solution1();
        ListNode new_head_1 = s1.deleteDuplicates(list.getHead());        
        while(new_head_1 != null){
            System.out.print(new_head_1.val + " ");
            new_head_1 = new_head_1.next;
        }
        
        System.out.println();
        
        Solution2 s2 = new Solution2();
        ListNode new_head_2 = s2.deleteDuplicates(list.getHead());
        while(new_head_2 != null){
            System.out.print(new_head_2.val + " ");
            new_head_2 = new_head_2.next;
        }
    }
}
