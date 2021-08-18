/**
 * Jared Scott 
 */

import java.io.BufferedReader;
import java.io.FileReader;

public class MaxPrioritySkewHeap {
    public Node root;
    private String title;
    private String indent = "    ";
    
    public MaxPrioritySkewHeap(String title) {
        this.title = title;
    }
    
    public void insert(Pair data) {
        //Creates a new node and merges it with the heap
        this.root = merge(this.root, new Node(data));
    }
    
    public Node removeMax() {
        //Since this is a max heap the max value is always the root. 
        if (this.root == null) {
            System.out.println("The Queue is Empty");
            return this.root;
        }
        else {
            Node temp = this.root;
            this.root = merge(this.root.left, this.root.right);
            return temp;
        }
    }
    
    public static Node merge(Node node1, Node node2) {
        //Checking to see if either node is null
        if (node1 == null) {
            return node2;
        }
        if (node2 == null) {
            return node1;
        }
        
        //Comparing the data and making the smaller of the two nodes a child of the larger
        if (node1.data.compareTo(node2.data) > 0) {
            Node temp = node1.left;
            node1.left = merge(node1.right, node2);
            node1.right = temp;
            return node1;   
        }
        else {
            Node temp = node2.right;
            node2.right = merge(node2.left, node1);
            node2.left = temp;
            return node2;
        }
    }
    
    public void printHeap() {
        //Helper method for the recursion
        System.out.println("Heap: " + this.title + "\n-----------------------");
        printHeap(this.root, this.indent);
        System.out.println("\n-----------------------");
    }
    public void printHeap(Node rootNode, String indent) {
        //Recursively prints our the heap marking the root.
        if (rootNode != null) {
            printHeap(rootNode.left, indent + this.indent);
            if (rootNode == this.root) {
                System.out.println("Root: " + rootNode.data);
            }
            else {
                System.out.println(indent + rootNode.data);
            }
            printHeap(rootNode.right, indent + this.indent);
        }
    }
            
    public class Node {
        public Pair data;
        public Node left;
        public Node right;
        
        public Node(Pair data) {
            this.data = data;
        }
    }
    
    public static void main(String[] args) {
        //Testing the heap functionality
        //Creating the two heaps
        MaxPrioritySkewHeap heap1 = new MaxPrioritySkewHeap("Heap1");
        MaxPrioritySkewHeap heap2 = new MaxPrioritySkewHeap("Heap2");
        //Arrays of data to fill the heaps
        String[] words1 = {"abandon", "ability", "able", "casino", "a", "abortion", "beef"};
        int[] freq1 = {1,12,30,16,17,8,5};
        String[] words2 = {"daughter", "beg", "begin", "carry", "cart"};
        int[] freq2 = {6,20,21,22,14};
        //Inserting data into the heaps
        for (int i = 0 ; i < 7 ; i++) {
            heap1.insert(new Pair(words1[i], freq1[i]));
        }
        for (int i = 0 ; i < 5 ; i++) {
            heap2.insert(new Pair(words2[i], freq2[i]));
        }
        //Displaying both heaps
        System.out.println("Printing Heap1\n");
        heap1.printHeap();
        System.out.println("\n\nPrinting Heap2\n");
        heap2.printHeap();
        //Demonstrating the merge method
        System.out.println("\n\nMerging the two heaps\n");
        MaxPrioritySkewHeap heap = new MaxPrioritySkewHeap("Heap Combined");
        heap.root =  merge(heap1.root,heap2.root);
        heap.printHeap();
        //Demonstrating the remove max method
        Node removed;
        System.out.println("\n\nDemonstrating the Remove Max Method\n\n");
        removed = heap.removeMax();
        System.out.println(removed.data + " Removed\n\n");
        heap.printHeap();
        removed = heap.removeMax();
        System.out.println("\n\n" + removed.data + " Removed\n\n");
        heap.printHeap();
        removed = heap.removeMax();
        System.out.println("\n\n" + removed.data + " Removed\n\n");
        heap.printHeap();
        removed = heap.removeMax();
        System.out.println("\n\n" + removed.data + " Removed\n\n");
        heap.printHeap();
    }
}