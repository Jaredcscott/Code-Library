import java.math.BigInteger;

/*
 * @author Jared Scott
 * 
 */

public class IsPalindrome {
    /*
	 * This class/method will determine if the supplied number (Big Integer capable) is a palindrome    
	 * ARGUMENTS:
	 * 	A number (Int) which you want to test
	 *
	 * OUTPUT:
	 *	boolean: true if the supplied number is a palindrome, false if not. 
	 */
    public static boolean isPalindrome(BigInteger num) {
        String numS = "" + num;
        if (numS.length() == 1) {
            return true;
        }
        else {
            int endInd = numS.length()-1;
            for (int i = 0; i < (numS.length()/2) ; i++) {
                if (numS.charAt(i) != numS.charAt(endInd)) {
                    return false;
                }
                endInd -= 1;
                
            }
            return true;
        }
    }
    
    public static void main(String[] args) {
        BigInteger num = new BigInteger("" + args[0]);
        boolean result = isPalindrome(num);
        System.out.println(result);
    }
}