/**
 *@author Jared Scott ☯ 
 *This class implements the quadratic equation. Allowing a user to find the real roots of a quadratic equation. 
 *Input is entered one element at a time separated by enter key presses. 
 */
import java.util.Scanner;
public class Quadratic{
    public static void main(String[] arg){
        Scanner userInput = new Scanner(System.in);
        System.out.print("Enter a, b, c: ");
        double a = userInput.nextDouble();
        double b = userInput.nextDouble();
        double c = userInput.nextDouble();
        double discriminant = Math.pow(b, 2) - (4 * a * c);
        if(discriminant > 0){
                System.out.println("There are two roots for the quadratic equation with these coefficients.");
                double root1 = (-b + Math.pow(discriminant,.5))/(2 * a);
                double root2 = (-b - Math.pow(discriminant,.5))/(2 * a);
                System.out.print("r1 = ");
                System.out.println(root1);
                System.out.print("r2 = ");
                System.out.println(root2);
        }
        if(discriminant == 0) {
            System.out.println("There is one root for the quadratic equation with these coefficients.");
            double root1 = (-b + Math.pow(discriminant, .5)) / (2 * a);
            System.out.print("r1 = ");
            System.out.println(root1);
        }
        if(discriminant < 0) {
            System.out.println("There are no roots for the quadratic equation with these coefficients.");
        }
    }
}
