/**
 *
 * @author Jared Scott
 * This class defines a Binary search tree, with the needed methods to insert, remove, search, and display the value
 * of each node in the tree. This file also contains the class definition for a node in the tree.
 *
 */
 
import java.lang.Comparable;

public class BinarySearchTree<E extends Comparable<E>> {
    public Node<E> root;
    public int nodeCount;

    public BinarySearchTree() {
    }

    public boolean insert(E value) {
        //Inserts values into the tree. In the process, the tree is 'scanned' to find the appropriate location to
        //insert the new value.
        if (this.root == null) {
            this.root = new Node<>(value);
            this.nodeCount += 1;
            return true;
        }
        else {
            Node<E> parent = null;
            Node<E> node = this.root;
            while (node != null) {
                parent = node;
                //value is greater than the node being checked
                if (node.value.compareTo(value) < 0) {
                    node = node.right;
                }
                //value is lesser than the node being checked
                else if (node.value.compareTo(value) > 0) {
                    node = node.left;
                }
                //value is equal to the node being checked
                else if (node.value.compareTo(value) == 0) {
                    return false;
                }
            }
            //Adding in new node
            Node<E> newNode = new Node<>(value);
            if (parent.value.compareTo(value) < 0) {
                parent.right = newNode;
                this.nodeCount += 1;
                return true;
            }
            else {
                parent.left = newNode;
                //Incrementing the node count variable
                this.nodeCount += 1;
                return true;
            }
        }
    }

    public boolean remove(E value) {
        //Removes values from the tree, 'scanning' through the tree to find the appropriate replacement for the
        //removed value
        if(!this.search(value)) {
            return false;
        }
        else {
            Node<E> parent = null;
            Node<E> node = this.root;
            boolean done = false;
            while (!done) {
                if (node.value.compareTo(value) < 0) {
                    parent = node;
                    node = node.right;
                }
                else if (node.value.compareTo(value) > 0) {
                    parent = node;
                    node = node.left;
                }
                else {
                    done = true;
                }
            }
            if (node.left == null) {
                if (parent == null) {
                    this.root = node.right;
                }
                else {
                    if(parent.value.compareTo(value) < 0) {
                        parent.right = node.right;
                    }
                    else {
                        parent.left = node.right;
                    }
                }
            }
            else {
                //Identifying the right-most node, this will be the largest value in that subtree.
                Node<E> parentRight = node;
                Node<E> rightMost = node.left;
                while (rightMost.right != null) {
                    parentRight = rightMost;
                    rightMost = rightMost.right;
                }
                node.value = rightMost.value;
                if(parentRight.right == rightMost) {
                    parentRight.right = rightMost.left;
                }
                else {
                    parentRight.left = rightMost.left;
                }
            }
        }
        //Decrementing the node count variable
        this.nodeCount -= 1;
        return true;
    }

    public boolean search(E value) {
        //Searches the tree for a given value
        Node<E> node = this.root;
        while (node != null) {
            if (node.value.compareTo(value) == 0) {
                return true;
            }
            else if (node.value.compareTo(value) < 0){
                node = node.right;
            }
            else if (node.value.compareTo(value) > 0) {
                node = node.left;
            }
        }
        return false;
    }

    public void inOrderTraverse(Node<E> curNode) {
        //Used to traverse the tree to count nodes
        if (curNode != null) {
            inOrderTraverse(curNode.left);
            System.out.println(curNode.value);
            inOrderTraverse(curNode.right);
        }
    }

    public void display(String message) {
        //Traverses the tree and displays the value of each node along the way
        System.out.println();
        System.out.println(message);
        Node<E> node = this.root;
        inOrderTraverse(node);
    }

    public int numberNodes() {
        //Returns the number of nodes in the tree
        return this.nodeCount;
    }

    public int countLeafNodes(Node<E> curNode) {
        //Recursively counts the number of leaf nodes
        if (curNode == null) {
            return 0;
        }
        if (curNode.left == null && curNode.right == null) {
            return 1;
        }
        else {
            return countLeafNodes(curNode.left) + countLeafNodes(curNode.right);
        }
    }

    public int numberLeafNodes() {
        //Returns the number of leaf nodes in the tree
        return countLeafNodes(this.root);
    }

    public int computeHeight(Node<E> node) {
        //Recursively counts the height of the tree
        if(node == null) {
            return -1;
        }
        else {
            //Determining which side (right or left) which is "taller"
            int leftHeight = computeHeight(node.left);
            int rightHeight = computeHeight(node.right);
            return 1 + Math.max(rightHeight, leftHeight);
        }
    }

    public int height() {
        //Returns the height of the tree
        return computeHeight(this.root);
    }

    public class Node<E extends Comparable<E>> {
        //Defines the Node class and its associated methods
        public E value;
        public Node left;
        public Node right;

        public Node (E value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        @Override
        public String toString() {
            return (String) this.value;
        }
    }
}