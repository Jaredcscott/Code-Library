/**
 *
 * @author Jared
 * This class defines the client logic for the chat system  
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) throws Exception {
        BufferedWriter writer;
        BufferedReader reader;
        Scanner scan;
        String response, send;
        
        Socket sck = new Socket("localhost",5555);
        reader = new BufferedReader(new InputStreamReader(sck.getInputStream()));
        writer = new BufferedWriter(new OutputStreamWriter(sck.getOutputStream()));
        scan = new Scanner(System.in);
        while(true) {
            send = scan.nextLine();
            writer.write(send + "\r\n");
            writer.flush();
            System.out.print("> "); 
            response = rd.readLine().trim();
            System.out.println("From Server: " + response);
            System.out.print("> ");   
        }   
    }
}