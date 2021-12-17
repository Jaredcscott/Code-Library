import java.util.ArrayList;
import java.util.Collections;

/*
 * @author Jared Scott ☯
 * This class will return the prime factros for any integer provided
 */
 
public class PrimeFactors {
	/*
	 * This class will return a list of the prime factors of a number 
	 * ARGUMENTS:
	 * 	Integer: The integer that you would like to find the prime factors for 
	 *
	 * OUTPUT:
	 *	Printed Array: An array holding all of the prime factors of the input number
	 */
	
	public static void main(String[] args) {
		ArrayList<Long> factors = new ArrayList<Long>();
		long num = Long.parseLong(args[0]);
		for (long i = 1; i <= Math.sqrt(num); i++) {
			if (num % i == 0 && factors.contains(i) == false && factors.contains(num/i) == false) {
				factors.add(i);
				factors.add(num/i);				
			}
		}
		Collections.sort(factors);
		ArrayList<Long> primeFactors = new ArrayList<Long>();
		ArrayList<Long> factorFactors =  new ArrayList<Long>();
		for (long factor : factors) {
			factorFactors.clear();
			for (long j = 1; j <= Math.sqrt(factor); j++) {
				if (factor % j == 0 && factorFactors.contains(j) == false) {
					factorFactors.add(j);
				}
			}

			if (factorFactors.size() == 1 && primeFactors.contains(factor) == false) {
				primeFactors.add(factor);
			}
		}
		System.out.println(primeFactors);
	}
}
