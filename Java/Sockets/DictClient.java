/**
 * @author Jared Scott ☯
 * 
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

public class DictClient {
    static String help = "--- DictClient Help ---\nUsage: java DictClient [words]\n"
            + "This class will use a dictionary protocol to connect to a dictionary\n"
            + "server and retrive definitions for the provided words";
    static String hostName =  "dict.org";
    static int portNum = 2628;
    static SocketAddress inetAddress = new InetSocketAddress(hostName, portNum);
    static Socket socket = new Socket();
    static InputStream inStream;
    static OutputStream outStream;
    static BufferedReader reader;
    static BufferedWriter writer;
    public static void main(String[] args) {
        System.out.println("--------------------------------------------");
        //When no arguments are provided the program prints the help message
        if(args.length == 0) {
            System.out.println(help);
            return;
        }
        try {
            socket.setSoTimeout(3000);
            socket.connect(inetAddress, 3000);
            inStream = socket.getInputStream();
            outStream = socket.getOutputStream();
            reader = new BufferedReader(new InputStreamReader(inStream));
            writer = new BufferedWriter(new OutputStreamWriter(outStream));
            int count = 0;
            while (count < args.length) {   
                int defCount = 1;
                String curWord = args[count];
                writer.write("DEFINE foldoc " + curWord + "\r\n");
                writer.flush();
                String output = "";
                boolean defReceived = false;
                while((output = reader.readLine()) != null){
                    if(output.startsWith("151 ")){
                        System.out.print("Definition of : " + curWord + "\n");
                        defReceived = true;
                        continue;
                    }
                    if (output.startsWith("250 ") && count != args.length -1 ) {
                        //This is to keep the system from exiting until the last definition is printed
                        System.out.println("--------------------------------------------");
                        break;
                    }
                    if (output.startsWith("250 ") && count == args.length -1){
                        System.out.println("--------------------------------------------");
                        writer.write("quit\r\n");
                        writer.flush();
                        break;
                    }
                    if (output.startsWith("552 ")){
                        System.out.println("No match found for the word: " + curWord + " in the database FOLDOC");
                        System.out.println("--------------------------------------------");
                        break;
                    }
                    if (defReceived) {
                        System.out.println(output);
                        defCount += 1;
                        continue;
                    }
                    defReceived = false;
                }
                count++;
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }   
    }
}