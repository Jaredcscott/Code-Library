import java.util.ArrayList;


public class FibonacciGenerator {
	public static void main(String[] args) {
		ArrayList<Integer> fibNums = new ArrayList<Integer>();
		fibNums.add(1);
		fibNums.add(2);
		int curNum = 3;
		while (curNum < args[2]) {
			fibNums.add(curNum);
			curNum = curNum + fibNums.get(fibNums.size() - 2);
		}
		int sum = 0;
		for (int value : fibNums) {
			if (value % 2 == 0) {
				sum += value;
			}
		}	
		System.out.println(sum);
	}
}