package LinkedList;
import java.util.Arrays;

public class SinglyLinkedList {

    public ListNode head;

    // Definition for singly-linked list.
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int x) {  val = x;  next = null;  }
    }

    /**
     * using data[] array to creating a singly-linked list
     * 
     * @param data, int array for linked-list
     * @return the head of the list
     */
    public ListNode createList(int[] data) {
        if(data.length == 0) return null;
      
        ListNode newNode = new ListNode(data[0]);
        newNode.next = createList(Arrays.copyOfRange(data, 1, data.length));
        
        return newNode;
    }
    
    /**
     * found the node at the position of index
     * @param index, the position index
     * @return ListNode
     */
    public ListNode foundbyIndex(int index) {
        ListNode current = head;
        int i = 0;
        while(current != null && i != index) {  
            current = current.next;
            i++;  
        }  
        return current;  
    }
    
    /**
     * found the node by value (the first appear one)
     * @param val, the value index
     * @return ListNode, if not found, return null
     */
    public ListNode foundbyValue(int val) {
        ListNode current = head;
        int v = 0;
        while(current != null && v != val) {
            current = current.next;
        }  
        return current;  
    }
    
}
