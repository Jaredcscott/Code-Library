/*
 * @author Jared Scott ☯
 * 
 */

import java.io.InputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

public class TimeClient {
    //Help message for when invalid input is entered
    static  String help = "--- TimeClient Help ---\nUsage: java TimeClient [host]\n"
            + "This class implements a Time Protocol which connects to an receives data from a web socket"; 
    static String hostName;
    static int portNum = 37;
    static TimeZone timeZone = TimeZone.getTimeZone("GMT");
    static Calendar calendar = Calendar.getInstance(timeZone);
    static InputStream inStream;
    static long milli = 0;
    static Socket socket;
    static ArrayList<String> events = new ArrayList<String>();
    static ArrayList<int[]> reminders =  new ArrayList<int[]>();
    /**
     * reminders ArrayList index meanings
     * 0:  year
     * 1:  month
     * 2:  date
     * 3:  hour
     * 4:  minute
     */
    
    public static void main(String[] args) {
        addReminders(); //Adding reminders to array
        //When no arguments are provided the program prints the help message
        if(args.length == 0) {
            System.out.println(help);
        }
        else {
            try{
                hostName = args[0];
                if (hostName.equals("") || hostName.indexOf('.') == -1) { //Performing some input validation on the hostname
                    System.out.println("Invalid Hostname Given");
                    return;
                }
                socket = new Socket(hostName, portNum);
                socket.setSoTimeout(3000);
                inStream = socket.getInputStream();
                for (int i = 0; i < 4; i++){
                    int curByte = inStream.read();
                    long milliShift = milli << 8; //Shifting the value of milli 
                    milli = milliShift | curByte; //Bitwise comparison 
                }  
                milli *= 1000; //Converting to seconds
                calendar.set(1900, 0, 1, 0, 0, 0);
                milli += calendar.getTimeInMillis();
                Date curDate = new Date(milli);
                System.out.println("The current date is: " + curDate);
                System.out.println("Checking reminders...\n");
                checkReminders(curDate);
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    
    public static void checkReminders(Date curTime){
        for (int i=0; i < reminders.size();i++){
            int[] rem = reminders.get(i);
            Date remDate = new Date(rem[0],rem[1],rem[2],rem[3],rem[4]);
            if(curTime.before(remDate)){
                System.out.println("Reminder: " + events.get(i)+ " is in the future.");
                System.out.println(events.get(i) + " will start on " + remDate.toString());            
            }
            else{
                System.out.println("Reminder: " + events.get(i)+ " is in the past");
                System.out.println("Removal from reminders list is suggested");
            }
            System.out.println();
        }
    }

    public static void addReminders() {
        int[] event1 = {2020-1900,8,29,7,30};
        reminders.add(event1);
        events.add("Ecommerce Meeting 1");
        int[] event2 = {2020-1900,9,6,7,30};
        reminders.add(event2);
        events.add("Ecommerce Meeting 2");
        int[] event3 = {2020-1900,9,11,11,59};
        reminders.add(event3);
        events.add("Exam 1");
    }
}