/**
 * @ Jared Scott
 * This class will construct a pyramid where the center number is always 1. 
 * The program accepts as input a number representing the desired pyramid height. 
 */

import java.util.Scanner;


public class CenteredPyramid {
    public static void main(String[] arg){
        //Setting up scanner to take input
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of lines: ");
        int userInput = input.nextInt();
        //main for loop to generate the rows.
        for(int row = 1; row <= userInput; row++){
            String spaceString = "";
            int count = 0;
            //identifying the amount of spaces that each number needs to be formatted correctly
            String inputString = "" + userInput;
            int cellWidth = inputString.length() + 1;
            int currentRowsSpaces = (userInput*cellWidth)-(row*cellWidth);
            //adding the appropriate amount of spaces before each row to align the numbers properly between rows
            while(count < currentRowsSpaces){
                spaceString += " ";
                count += 1;
                }
            //the first row behaves different than the other rows, special case for the first row here
            if(row == 1){
                String format = "%" + cellWidth + "s";
                String firstRow = "";
                int count1 = 1;
                while(count1 < cellWidth){
                    firstRow += " ";
                    count1 += 1;
                }
                firstRow += "" + 1 + "\n";
                System.out.print(spaceString);
                System.out.printf(format,firstRow);
                continue;
            }
            //this section deals with all other rows aside from row 1
            System.out.print(spaceString);
            for(int columns = row + 2; columns > 0 ; columns-=(row+cellWidth)){
                int currentNum = row;
                //creating format with a variable cell width
                String format = "%" + cellWidth + "s";
                //this will decrease the number until it reaches 1
                while(currentNum > 0){
                    String currentNumString = "" + currentNum;
                    System.out.printf(format,currentNumString);
                    currentNum -= 1;
                }
                currentNum = 1;
                //This will increase form 1 till the row number
                while(currentNum < row) {
                    currentNum += 1;
                    String currentNumString = "" + currentNum;
                    System.out.printf(format, currentNumString);
                }
                System.out.print("\n");
            }
        }       
    }    
}