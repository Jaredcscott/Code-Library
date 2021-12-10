/**
 * @author Jared Scott ☯
 * 
 * This class defines a Spell Checking tool. The program will read in a dictionary file of words, and generate a binary
 * search tree containing all of the words in the dictionary file. The program will display stats on the tree, as well
 * as demonstrating the capability to correctly generate a binary search tree
 *
 */
import java.util.ArrayList;

public class SpellChecker {
    public static void main(String[] args) {

        // Step 1: Demonstrate tree capabilities
        testTree();

        // Step 2: Read the dictionary and report the tree statistics
        BinarySearchTree<String> dictionary = readDictionary();
        reportTreeStats(dictionary);

        // Step 3: Perform spell checking
        java.io.File file = new java.io.File("Letter.txt");
        try (java.util.Scanner input = new java.util.Scanner(file)) {
            System.out.println("\n-- Misspelled Words --");
            while (input.hasNext()){
                String word = input.next().replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
                if(!dictionary.search(word)) {
                    System.out.println(word);
                }
                else {
                    //Word is already in your dictionary BST
                }
            }
        }
        catch (java.io.IOException ex) {
            System.out.println("File not found, or file unreadable.");
        }
    }

    /**
     * This method is used to help develop the BST, also for the grader to
     * evaluate if the BST is performing correctly.
     */
    public static void testTree() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        //
        // Add a bunch of values to the tree
        tree.insert("Olga");
        tree.insert("Tomeka");
        tree.insert("Benjamin");
        tree.insert("Ulysses");
        tree.insert("Tanesha");
        tree.insert("Judie");
        tree.insert("Tisa");
        tree.insert("Santiago");
        tree.insert("Chia");
        tree.insert("Arden");

        //
        // Make sure it displays in sorted order
        tree.display("--- Initial Tree State ---");
        reportTreeStats(tree);

        //
        // Try to add a duplicate
        if (tree.insert("Tomeka")) {
            System.out.println("oops, shouldn't have returned true from the insert");
        }
        tree.display("--- After Adding Duplicate ---");
        reportTreeStats(tree);

        //
        // Remove some existing values from the tree
        tree.remove("Olga");    // Root node
        tree.remove("Arden");   // a leaf node
        tree.display("--- Removing Existing Values ---");
        reportTreeStats(tree);

        //
        // Remove a value that was never in the tree, hope it doesn't crash!
        tree.remove("Karl");
        tree.display("--- Removing A Non-Existent Value ---");
        reportTreeStats(tree);
    }

    /**
     * This method is used to report on some stats about the BST
     */
    public static void reportTreeStats(BinarySearchTree<String> tree) {
        System.out.println("-- Tree Stats --");
        System.out.printf("Total Nodes : %d\n", tree.numberNodes());
        System.out.printf("Leaf Nodes  : %d\n", tree.numberLeafNodes());
        System.out.printf("Tree Height : %d\n", tree.height());
    }

    /**
     * This method reads the dictionary and constructs the BST to be
     * used for the spell checking.
     */
    public static BinarySearchTree<String> readDictionary() {
        ArrayList<String> dictionary = new ArrayList<>();
        BinarySearchTree<String> tree = new BinarySearchTree<>();
        java.io.File file = new java.io.File("Dictionary.txt");
        try (java.util.Scanner input = new java.util.Scanner(file)) {
            while (input.hasNext()) {
                String line = input.nextLine().toLowerCase();
                //Removing all non-alpha characters
                String curLine = line.replaceAll("[^a-zA-Z]", "").toLowerCase();
                if(tree.search(curLine)) {
                    continue;
                }
                else {
                    dictionary.add(curLine);
                }
            }
        }
        catch (java.io.IOException ex) {
            System.out.println("File not found, or file unreadable.");
        }
        //Shuffling the array prior to inserting the array elements into the BST
        java.util.Collections.shuffle(dictionary, new java.util.Random(System.currentTimeMillis()));
        for (int i = 0; i < dictionary.size(); i++) {
            tree.insert(dictionary.get(i));
        }
        return tree;
    }
}