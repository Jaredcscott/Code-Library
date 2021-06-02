import java.util.ArrayList;
import java.util.Arrays;

public class FibonacciGenerator {
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