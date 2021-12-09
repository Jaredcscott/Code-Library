/*
 * @author Jared Scott ☯
 * 
 */

import java.util.ArrayList;
import java.util.Collections;
 
public class Palindromes {
    /*
	 * This class will find the palindromes that can be formed by multiplying two 3 digit numbers   
	 * ARGUMENTS:
	 * 	none
	 *
	 * OUTPUT:
	 *	Printed Array: An array holding palindromic numbers which can be formed by the product of two numbers which are 3 digits or less.  
	 */
    
	public static void main(String[] args) {
		ArrayList<Integer> palindromes = new ArrayList<Integer>();
		for (int i = 100; i < 1000; i++) {
			for (int j = 100; j < 1000; j++){
				int num = i * j;
				boolean isPalindrome = true;
				String numString = Integer.toString(num);
				int endIndex = numString.length() - 1;
				int start = 0;
				while (isPalindrome) {	
					isPalindrome = numString.charAt(start) == numString.charAt(endIndex);
					if (start == endIndex || start == numString.length() / 2) {
						break;
					}
					start += 1;
					endIndex -= 1;
				}
				if (isPalindrome) {
					palindromes.add(num);
				}
			}
		}
		Collections.sort(palindromes);
        System.out.println(palindromes);
	}	
}