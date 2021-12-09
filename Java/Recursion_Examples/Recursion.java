/**
 * @author Jared Scott ☯
 * This class defines a few examples of recursion.
 */

public class Recursion {
    public static void main(String[] args) {

        int[] sumMe = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        System.out.printf("Array Sum: %d\n", arraySum(sumMe, 0));

        int[] minMe = { 0, 1, 1, 2, 3, 5, 8, -42, 13, 21, 34, 55, 89 };
        System.out.printf("Array Min: %d\n", arrayMin(minMe, 0));

        String[] amISymmetric =  {
                "You can cage a swallow can't you but you can't swallow a cage can you",
                "I still say cS 1410 is my favorite class"
        };
        for (String test : amISymmetric) {
            String[] words = test.toLowerCase().split(" ");
            System.out.println();
            System.out.println(test);
            System.out.printf("Is word symmetric: %b\n", isWordSymmetric(words, 0, words.length - 1));
        }

        double weights[][] = {
                { 51.18 },
                { 55.90, 131.25 },
                { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };
        System.out.println();
        System.out.println("--- Weight Pyramid ---");
        for (int row = 0; row < weights.length; row++) {
            for (int column = 0; column < weights[row].length; column++) {
                double weight = computePyramidWeights(weights, row, column);
                System.out.printf("%.2f ", weight);
            }
            System.out.println();
        }

        char image[][] = {
                {'*','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ','*','*',' ',' '},
                {' ','*',' ',' ','*','*','*',' ',' ',' '},
                {' ','*','*',' ','*',' ','*',' ','*',' '},
                {' ','*','*',' ','*','*','*','*','*','*'},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ','*','*','*',' ',' ','*',' '},
                {' ',' ',' ',' ',' ','*',' ',' ','*',' '}
        };
        int howMany = howManyOrganisms(image);
        System.out.println();
        System.out.println("--- Labeled Organism Image ---");
        for (char[] line : image) {
            for (char item : line) {
                System.out.print(item);
            }
            System.out.println();
        }
        System.out.printf("There are %d organisms in the image.\n", howMany);

    }

    public static long arraySum(int[] data, int position) {
        //Recursively sums the values in a given array
        if (data.length == 0) {
            return 0;
        }
        if(data.length - 1 == position) {
            return data[position];
        }
        return data[position] + arraySum(data, position + 1);
    }

    public static long arrayMin(int[] data, int position) {
        //Recursively finds the smallest value in an array
        if(position == data.length - 1) {
            return data[data.length - 1];
        }
        return Math.min(data[position + 1], arrayMin(data,position + 1));
    }

    public static boolean isWordSymmetric(String[] words, int start, int end) {
        //Recursively checks if a sentence is symmetric
        if (words.length == 0) {
            return true;
        }
        if (!(words[start]).toLowerCase().equals(words[end].toLowerCase())) {
            //checking if the words are the same
            return false;
        }
        else if (start == end) {
            return true;
        }
        return isWordSymmetric(words, start + 1, end - 1);
    }

    public static double computePyramidWeights(double[][] weights, int row, int column) {
        //Recursively calculates the weight load placed upon each block in a pyramid.
        if (row < 0) {
            //checking if row is negative
            return 0;
        }
        if (column < 0) {
            //checking if column is negative
            return 0;
        }
        if (weights.length == 0) {
            //checking if the array is empty
            return 0;
        }
        if (weights.length <= row) {
            //checking is row is greater than our pyramid size
            return 0;
        }
        if (weights[row].length <= column) {
            //checking if column is greater than our pyramid size
            return 0;
        }
        if (row == 0) {
            //top row, only one block
            return weights[0][0];
        }
        else if (column == 0) {
            return computePyramidWeights(weights, row - 1, column) / 2 + weights[row][column];
        }
        else if (column == weights[row].length - 1) {
            return computePyramidWeights(weights, row - 1, column - 1) / 2 + weights[row][column];
        }
        else {
            return computePyramidWeights(weights, row - 1, column) / 2 + computePyramidWeights(weights, row - 1, column - 1) / 2 + weights[row][column];
        }
    }

    public static boolean recursiveArrayCheck(char[][] image, int row, int column, char label) {
        //Recursively checks the values above, right, left, and below, a given value in a multi dimensional array.
        if (row < 0) {
            //checking if row is negative
            return false;
        }
        if (column < 0) {
            //checking if column is negative
            return false;
        }
        if ( row >= image.length) {
            //checking if row is larger than our image
            return false;
        }
        if (column >= image[row].length) {
            //checking if column is larger than our image
            return false;
        }
        if (image[row][column] != '*') {
            //checking if a space is empty
            return false;
        }
        if (image[row][column] == label) {
            //checking is a space has already been labeled
            return true;
        }
        //labeling an astrix
        image[row][column] = label;
        recursiveArrayCheck(image, row - 1, column, label);
        recursiveArrayCheck(image, row + 1, column, label);
        recursiveArrayCheck(image, row, column - 1, label);
        recursiveArrayCheck(image, row, column + 1, label);
        return true;
    }

    public static int howManyOrganisms(char[][] image) {
        //Counts the number of organisms in a given multidimensional array
        int organisms = 0;
        char curLabel = 'a';
        for ( int i = 0; i < image.length; i++) {
            for ( int j = 0; j < image[i].length; j++) {
                if (recursiveArrayCheck(image, i, j, curLabel)) {
                    organisms++;
                    curLabel++;
                }
            }
        }
        return  organisms;
    }
}