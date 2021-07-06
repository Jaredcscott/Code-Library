/**
 * @ Jared Scott
 * A01203464
 * cs 1410
 *
 * hw 1 Pyramid
 */

import java.util.Scanner;


public class pyramid2 {
    public static void main(String[] arg){
        //Setting up scanner to take input
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of lines: ");
        int userInput = input.nextInt();
        //Main loop to generate rows
        for(int row = 1; row <= userInput; row++){
            String spaceString = "";
            int count = 0;
            //identifying what the Largest number will be
            double maxNum = Math.pow(2,userInput - 1);
            long maxNumLong = Math.round(maxNum);
            //identifying the amount of spaces that each number needs to be formatted correctly
            String inputString = "" + maxNumLong;
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
            //For loop to generate the lines after the first line
            System.out.print(spaceString);
            for(int columns = row + 2; columns > 0 ; columns-=(row+cellWidth)){
                int currentNum = 1;
                //Creating the format string for the printf
                String format = "%" + cellWidth + "s";
                double maxNumOnRow = Math.pow(2, row);
                //thie will alter the current num value for the current row
                while(currentNum < maxNumOnRow){
                    String currentNumString = "" + currentNum;
                    System.out.printf(format,currentNumString);
                    currentNum *= 2;
                }
                currentNum /= 2;
                //dividing back to 1
                while(currentNum > 1){
                    currentNum /= 2;
                    String currentNumString = "" + currentNum;
                    System.out.printf(format,currentNumString);
                }
                System.out.print("\n");
            }
        }       
    }
}