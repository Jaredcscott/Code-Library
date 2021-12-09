/*
 * @author Jared Scott ☯
 * 
 */
public class PythagoreanTriples {
    /*
	 * This script will identify a single Pythagorean triple, whose sum (a+b+c) is 1000. 
     * A Pythagorean triple is a set of numbers with this relationship a^2 + b^2 = c^2
	 * ARGUMENTS:
	 * 	    None
	 *
	 * OUTPUT:
	 *	    The Pythagorean triple which meets the above mentioned requirement IE a + b + c = 1000  
	 */
     
    
    public static void main(String[] args){
        int product = 0;
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                for (int k = 0; k < 1000; k++) {
                    if ((i * i) + (j * j) == (k * k) && i < j && i < k && j < k) {
                        if ((i + j + k) == 1000) {
                            product = i * j * k;
                            System.out.println("Pythagorean triplet found : " + i + "," + j + "," + k);
                            System.out.println("Solution: " + product);
                        }
                    }
                }
            }
        }
    }
}