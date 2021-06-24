/**
 *@Author: Jared Scott 
 *This is a java implementation of a min heap (a data structure where the 'top' of the 'heap' is the minimum node within a tree (root).
 */

public static class MinHeap { 
        public Node[] Heap; 
        private int size; 
        private int maxsize; 

        private static final int FRONT = 1;

        public MinHeap(int maxsize) 
        { 
            this.maxsize = maxsize; 
            this.size = 0; 
            Heap = new Node[this.maxsize + 1]; 
            Heap[0] = new Node(new TeamSortingTool.Sort(new ArrayList<TeamSortingTool.Team>())); 
        } 
        
        public class Node {
            TeamSortingTool.Sort sort;
            private int score;
            public Node(TeamSortingTool.Sort sort){
                this.sort = sort;
                this.score = this.sort.getScore();
                
                if (this.score > 0 && (TeamSortingTool.sortLow == null || this.score < TeamSortingTool.sortLow.getScore())) {
                    TeamSortingTool.sortLow = this.sort;
                    System.out.println("NEW LOW!!: " + this.sort.getScore());
                }
            }
        }

        // Function to return the position of 
        // the parent for the node currently 
        // at pos 
        private int parent(int pos) 
        { 
            return pos / 2; 
        } 

        // Function to return the position of the 
        // left child for the node currently at pos 
        private int leftChild(int pos) 
        { 
            return (2 * pos); 
        } 

        // Function to return the position of 
        // the right child for the node currently 
        // at pos 
        private int rightChild(int pos) 
        { 
            return (2 * pos) + 1; 
        } 

        // Function that returns true if the passed 
        // node is a leaf node 
        private boolean isLeaf(int pos) 
        { 
            if (pos >= (size / 2) && pos <= size) { 
                return true; 
            } 
            return false; 
        } 

        // Function to swap two nodes of the heap 
        private void swap(int fpos, int spos) 
        { 
            Node tmp; 
            tmp = Heap[fpos]; 
            Heap[fpos] = Heap[spos]; 
            Heap[spos] = tmp; 
        } 

        // Function to heapify the node at pos 
        private void minHeapify(int pos) 
        { 

            // If the node is a non-leaf node and greater 
            // than any of its child 
            if (!isLeaf(pos)) { 
                if (Heap[pos].score > Heap[leftChild(pos)].score 
                    || Heap[pos].score > Heap[rightChild(pos)].score) { 

                    // Swap with the left child and heapify 
                    // the left child 
                    if (Heap[leftChild(pos)].score > Heap[rightChild(pos)].score) { 
                        swap(pos, leftChild(pos)); 
                        minHeapify(leftChild(pos)); 
                    } 

                    // Swap with the right child and heapify 
                    // the right child 
                    else { 
                        swap(pos, rightChild(pos)); 
                        minHeapify(rightChild(pos)); 
                    } 
                } 
            } 
        } 

        // Function to insert a node into the heap 
        public void insert(TeamSortingTool.Sort element) 
        { 
            Node curNode = new Node(element);
            if (size >= maxsize) { 
                return; 
            } 
            Heap[++size] = curNode; 
            int current = size; 

            while (Heap[current].score < Heap[parent(current)].score) { 
                swap(current, parent(current)); 
                current = parent(current); 
            } 
        } 
        
        public Node[] getHeap() 
        { 
            return this.Heap;
        } 

        // Function to print the contents of the heap 
        public void print() 
        { 
            for (int i = 1; i <= size / 2; i++) { 
                System.out.print(" PARENT : " + Heap[i].score 
                                 + " LEFT CHILD : " + Heap[2 * i].score 
                                 + " RIGHT CHILD :" + Heap[2 * i + 1].score); 
                System.out.println();
            }
            
        } 

        // Function to build the min heap 
        public void minHeap() 
        { 
            for (int pos = (size / 2); pos >= 1; pos--) { 
                minHeapify(pos); 
            } 
        } 

        // Function to remove and return the minimum 
        // element from the heap 
        public TeamSortingTool.Sort removeMin() 
        { 
            TeamSortingTool.Sort popped = Heap[FRONT].sort;
            Heap[FRONT] = Heap[size--]; 
            minHeapify(FRONT);
            return popped; 
        } 
    }
