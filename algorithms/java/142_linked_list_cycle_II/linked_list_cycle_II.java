import LinkedList.SinglyLinkedList;
import LinkedList.SinglyLinkedList.ListNode;

/**
 * @author Peng
 *
 * Problem Description:
 *      Given a linked list, return the node where the cycle begins. 
 *      If there is no cycle, return null.
 *      Note: Do not modify the linked list.
 *      Follow up:Can you solve it without using extra space?
 */
public class linked_list_cycle_II {

    /**
     * Solution 1:
     *      1st: using two runner(faster and slower) to check if there is a cycle.
     *      2nd: and a walker starting from the head.
     *           once two runner meet(exists cycle), slower cycling to check if could meet walker.
     *           if meet, walker is the cycle begin;
     *           if not, slower moving one cycle, walker move to next.
     *      
     * @param head, of the singly linked-list
     * @return begin, begin ListNode of the cycle
     *         if has no cycle, return null
     */
    public static ListNode detectCycle_1(ListNode head) {
        if(head == null)  return null;
        
        ListNode begin = head;
        ListNode tmp = null;
        // check if cycle exists
        ListNode fast = head;
        ListNode slow = head;
        
        while(slow.next != null && fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow) {
                tmp = slow;  // using tmp to record the slow cycling start position
                break;  // cycle existed
            }
        }
        if(tmp == null) return null;  // no cycle
        
        // cycling for slow
        while(begin != slow){
            slow = slow.next;
            if(tmp == slow) {
                begin = begin.next; // one cycle finished
            }
        }
            
        return begin;
    }

    /**
     * Solution 2:
     *      one pointer start from the meeting node.
     *      another start from the head.
     *      and the meet node is the begin
     *      
     *  Conduction:
     *      |-------s------|-------------r------------|
     *                     |-------t-------|          |
     *      |--------------k---------------|               
     *      ooooooooooooooooooooooooooooooooooooooooooo
     *      |              |               |          |
     *    head           begin         meet_node
     *    
     *      1st: two pointer: fast & slow, 
     *           fast: 2 node for 1 step; slow: 1 node for 1 step;
     *           if there is a cycle, fast will meet slow at meet_node;
     *           set that fast moves 2k node; slow k steps;
     *           
     *      2nd: 2k-k=nr=k=s+t ->  nr-t=s
     *           so. set two pointer (1 node a step) start from meet_node and head
     *               they will meet at begin;
     *              
     * @param head
     * @return
     */
    public static ListNode detectCycle_2(ListNode head) {
        if(head == null)  return null;
        
        ListNode begin = null;
        // check if cycle exists
        ListNode fast = head;
        ListNode slow = head;
        
        while(slow.next != null && fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow) {  // cycle exists, then find begin here
                begin = head;
                while(slow != begin) {
                    slow = slow.next;
                    begin = begin.next;
                }
                break;
            }
        }
        
        return begin;
    }
    
    /**
     * helper function: print the linked-list
     * @param h
     * @param maxlen, control the print length
     */
    public static void printList(ListNode h, int maxlen) {
        int i = 0;
        while(h != null && i < maxlen) {
            System.out.printf("%d  ", h.val);   
            h = h.next;
            i++;
        }
    }
    
    // test code
    public static void main(String[] args) {
        // create a singly linked list
        int[] data = {1, 2, 3, 4, 5};
        SinglyLinkedList list = new SinglyLinkedList();
        list.head = list.createList(data);        
        
        // add a cycle
        ListNode tail = list.foundbyIndex(4);
        tail.next = list.foundbyIndex(4);
        printList(list.head, 20);
        
        System.out.println();
        ListNode begin = detectCycle_2(list.head);
        if(begin != null) {
            System.out.println("the begin node of cycle is: " + begin.val);
        }
        else {
            System.out.println("there has no cycle.");
        }
    }

}
