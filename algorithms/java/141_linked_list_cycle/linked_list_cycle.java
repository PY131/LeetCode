import LinkedList.SinglyLinkedList;
import LinkedList.SinglyLinkedList.ListNode;

/**
 * @author Peng
 *
 * Problem Description:
 *      Given a linked list, determine if it has a cycle in it.
 *      Follow up: Can you solve it without using extra space?
 */
public class linked_list_cycle {

    /**
     * Solution 1:
     *      Considering of a fast runner and a slow walker moving in the linked-list.
     *      if cycle existed, the faster one will catch up the slow one by some cycles.  
     *  for more:   
     *      if the faster's speed is twice as much as the slower's, slower will be 
     *      caught up no more than two cycles of the singly-linked-list
     *      
     * @param head of the list
     * @return true if
     */
    public static boolean hasCycle_1(ListNode head) {
        if(head == null)  return false;
        ListNode fast = head;
        ListNode slow = head;
        
        while(slow.next != null && fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow) return true;
        }
        return false;
    }
    
    /**
     * helper function: print the list
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
        tail.next = list.foundbyIndex(2);
        printList(list.head, 20);
        System.out.println();
        System.out.println("the singly linked-list has cycle? " + hasCycle_1(list.head));
    }

}
