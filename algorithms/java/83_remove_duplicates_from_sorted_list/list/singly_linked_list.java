package list;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * 
 * @author Peng
 *
 * create a linked-list to store items using generic
 */
public class singly_linked_list<Item> {
    
    private ListNode head;   // head node
    private int N;  // list length
    
    // constructor
    public singly_linked_list(){
        head = null;
        N = 0;
    }
    
    // Definition for singly-linked list.
    public class ListNode {
        public Item val;
        public ListNode next;
        public ListNode(Item x) { val = x; next = null; }
    }
    
    /**
     * judge if is empty
     * @return true if is empty
     */
    public boolean isEmpty(){
        return N == 0;
    }
    
    /**
     * get the list's length
     * @return the length
     */
    public int length(){
        return N;
    }
    
    /**
     * get the head node 
     * @return the head node
     */
    public ListNode getHead(){
        return head;
    }
    
    
    /**
     * get the node with index without remove it
     * @param index
     * @return the head node
     */
    public ListNode getNode(int index){
        if(index < 1 || index > N){
            throw new NoSuchElementException();
        }
        ListNode node = head;
        for(int i = 0; i <= N; i++){
            if(i == index) break;
            else{
                node = node.next;
            }
        }
        return node;
    }
    
    /**
     * add node to the end
     * @param x is the adding item
     * @return true if add succeed
     */
    public void addNode(Item x){
        ListNode newNode = new ListNode(x);
        if (head == null) {
            head = newNode;
            N++;
        }
        else{
            ListNode tmp = head;
            while (tmp.next != null) {
                tmp = tmp.next;
            }
            tmp.next = newNode;
            N++;
        }
    }
    
    /**
     * add node to the index position
     * @param x is the adding item
     * @param index is the adding position
     * @return true if add succeed
     */
    public boolean addNode(Item x, int index){
        ListNode newNode = new ListNode(x);
        if(index < 1 || index > N+1){
            throw new UnsupportedOperationException();
        }
        
        if (index == 1) {
            newNode.next = head;
            head = newNode;
            N++;
            return true;
        }
        else{
            ListNode prev_node = head;
            ListNode now_node = head;
            for(int i = 0; i < N; i++){
                if(i == index){
                    newNode.next = prev_node.next;
                    prev_node.next = newNode;
                    N++;
                    return true;
                }
                prev_node = now_node;
                now_node = now_node.next;
            }
        }
        return false;
    }
    
    /**
     * delete a node at index
     * @param index
     * @return true if delete succeed
     */
    public boolean deleteNode(int index){
        if(index < 1 || index > N){
            throw new NoSuchElementException();
        }
        if(index == 1){
            head = head.next;
            return true;
        }
        
        ListNode prev_node = head;
        ListNode now_node = head;
        for(int i = 0; i < N; i++){
            if(i == index){
                prev_node.next = now_node.next;
                return true;
            }
            prev_node = now_node;
            now_node = now_node.next;
        }
        return false;
    }
    
}
    
    
    
    
   