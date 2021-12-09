/**
 * @author Jared Scott ☯
 * 
 */

import java.text.DecimalFormat;
import java.util.Properties;
import java.text.NumberFormat;


public class SysInfo {
	//This class shows how to display system statistics using Java
    public static void main(String[] args) {
        for (String arg : args) {
            switch (arg) {
                case "-cpu":
					//Displays the number of processors 
                    System.out.printf("Processors   :%15s\n", Runtime.getRuntime().availableProcessors());
                    break;
                case "-mem":
					//Displays information regarding the system's available memory 
                    DecimalFormat numFormat = new DecimalFormat("#");
                    numFormat.setGroupingUsed(true);
                    numFormat.setGroupingSize(3);
                    System.out.printf("Free Memory  :%15s\n", numFormat.format(Runtime.getRuntime().freeMemory()));
                    System.out.printf("Total Memory :%15s\n", numFormat.format(Runtime.getRuntime().totalMemory()));
                    System.out.printf("Max Memory   :%15s\n", numFormat.format(Runtime.getRuntime().maxMemory()));
                    break;
                case "-dirs":
					//Displays information regarding the current working directory 
                    System.out.println("Working Directory   : " + System.getProperty("user.dir"));
                    System.out.println("User Home Directory : " + System.getProperty("user.home"));
                    break;
                case "-os":
					//Displays information about the operating system 
                    System.out.println("OS Name             : " + System.getProperty("os.name"));
                    System.out.println("OS Version          : " + System.getProperty("os.version"));
                    break;
                case "-java":
					//Displays information about the installed Java system 
                    System.out.println("Java Vendor         : " + System.getProperty("java.vendor"));
                    System.out.println("Java Runtime        : " + System.getProperty("java.runtime.name"));
                    System.out.println("Java Version        : " + System.getProperty("java.version"));
                    System.out.println("Java Vm Version     : " + System.getProperty("java.vm.version"));
                    System.out.println("Java Vm Name        : " + System.getProperty("java.vm.name"));
                    break;
				default :
					System.out.println("Invalid Argument given: " + arg);
            }
        }
    }
}