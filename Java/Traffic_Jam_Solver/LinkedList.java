/**
 *
 * @author Jared Scott
 * 
 */
public class LinkedList {
    public ListNode head;
    public static int ListLength;
    
    //Defines the class for the nodes in the LinkedList.
    //List added to the name to help distinguish ListNodes from the class "Node"
    public static class ListNode {
        public Node data;
        public ListNode next;
        
        public ListNode(Node state) {
            this.data = state;
            this.next = null;
        }
    }
    
    //Defines a method to add a new ListNode to the end of the provided list
    public static LinkedList insert(LinkedList list, Node state) {
        ListNode newNode = new ListNode(state);
        newNode.next = null;
        
        if (list.head == null) {
            list.head = newNode;
        }
        else {
            ListNode curNode = list.head;
            while (curNode.next != null) {
                curNode = curNode.next;
            }
            curNode.next = newNode;
        }
        list.ListLength += 1;
        return list;
    }
    
    //Defines a method to remove the head from the provided list
    public static LinkedList removeHead(LinkedList list){
        ListNode temp = list.head;
        list.head = temp.next;
        temp.next = null;
        list.ListLength -= 1;
        return list;
    }
}