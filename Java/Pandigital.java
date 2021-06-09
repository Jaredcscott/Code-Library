/*
 * @author Jared Scott
 * 
 */
public class Pandigital{
    /*
	 * This class will print return a true if the given number is pandigital IE contains all digits 1-9 at most once 
	 * ARGUMENTS:
	 * 	Integer: a number (Long) which you want to test if it is pandigital  
	 *
	 * OUTPUT:
	 *	Boolean: true if the the number is pandigital, false if not
	 */
    public static boolean isPandigital(Long num) {
        boolean dupNums = false;
        String numString = "" + num;
        boolean[] nums = new boolean[9];
        if ( numString.length() == 9 ) {
            for (int i = 1 ; i <= numString.length(); i++) {
                char c = numString.charAt(i-1);
                Integer index = Character.getNumericValue(c);
                if (index == 0) {
                    return false;
                }
                //System.out.println(index);
                if(!nums[index-1]) {
                    nums[index-1] = true;
                }
                else {
                    //System.out.println(index);
                    dupNums = true;
                }
            }
        }
        else {
            return false; //"Failure!"
        }
        return !dupNums ; //? "Success! " + numString : "Failure!"
    }
    
    public static void main(String[] args) {
        System.out.println(isPandigital(Long.parseLong(args[0])));
    }
}

