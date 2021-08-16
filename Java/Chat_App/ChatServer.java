/**
 *
 * @author Jared
 * This class defines the server logic for the chat system  
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class ChatServer {
    public static void main(String[] args) throws Exception {
        ServerSocket sv = new ServerSocket(5555);
        BufferedWriter writer;
        BufferedReader reader;
        Scanner scan;
        Socket sck;
        String response, send;
        while(true) {
            System.out.println("Waiting for Client connection: ");
            sck = sv.accept();
            reader = new BufferedReader(new InputStreamReader(sck.getInputStream()));
            writer = new BufferedWriter(new OutputStreamWriter(sck.getOutputStream()));
            scan = new Scanner(System.in);

            while(true) {
                response = reader.readLine().trim();
                System.out.println("From Client: " + response);
                System.out.print("> ");
                send = scan.nextLine();
                writer.write(send + "\r\n");
                writer.flush();
                System.out.print("> "); 
            }
        }
    }
}