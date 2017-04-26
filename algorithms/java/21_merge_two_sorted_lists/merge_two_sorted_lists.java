
import LinkedList.SinglyLinkedList;
import LinkedList.SinglyLinkedList.ListNode;

/**
 * @author Peng
 * 
 * Problem Description:
 *  
 */
public class merge_two_sorted_lists {

    
    public static ListNode mergeTwoLists1(ListNode l1, ListNode l2) {
        if(l1 == null)  return l2;
        if(l2 == null)  return l1;
        
        if(l1.val <= l2.val){
            l1.next = mergeTwoLists1(l1.next, l2);
            return l1;
        }
        else{
            l2.next = mergeTwoLists1(l2.next, l1);
            return l2;
        }
    }
    
    // test code
    public static void main(String[] args) {
        // create a singly linked list
        int[] data1 = {1, 3, 5, 7, 9};
        int[] data2 = {2, 4, 6, 8, 10};
        SinglyLinkedList list1 = new SinglyLinkedList();
        SinglyLinkedList list2 = new SinglyLinkedList();
        list1.head = list1.createList(data1);     
        list2.head = list2.createList(data2);  
        
        ListNode l = mergeTwoLists1(list1.head, list2.head);
        
        while(l != null) {
            System.out.printf(l.val + " ");
            l = l.next;
        }
    }

}
