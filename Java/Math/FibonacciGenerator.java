import java.util.ArrayList;
import java.util.Arrays;

/*
 * @author Jared Scott
 * 
 */
 
public class FibonacciGenerator {
	/*
	 * This class will print a list containing a specified amount of fibonacci numbers  
	 * ARGUMENTS:
	 * 	Integer: The amount of fibonacci numbers you would like to generate 
	 *
	 * OUTPUT:
	 *	Printed Array: An array holding the desired number of fibonacci numbers 
	 */
	public static void main(String[] args) {
		ArrayList<Integer> fibNums = new ArrayList<Integer>();
		fibNums.add(1);
		fibNums.add(2);
		int curNum = 2;
		while (curNum < Integer.parseInt(args[0])) {
			fibNums.add(fibNums.get(fibNums.size()-2) +fibNums.get(fibNums.size()-1));
			curNum += 1;
		}
		System.out.println(fibNums);
	}
}