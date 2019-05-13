//package app;
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.io.OutputStreamWriter;
//import java.io.PrintWriter;
//import java.net.Socket;
//import java.net.UnknownHostException;
//
//
//public class TestServerSocket {
//    static Thread sent;
//    static Thread receive;
//    static Socket socket;
//
//    public static void main(String args[]) throws IOException, InterruptedException {
//
//        //socket = new Socket("127.0.0.1", 60563);
//        socket = new Socket("127.0.0.1", 60563);
//        while (true) {
//            socket = new Socket("127.0.0.1", 60563);
//            BufferedReader stdIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
//            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
//            System.out.println("Trying to read...");
//            String in = stdIn.readLine();
//            System.out.println(in);
//            out.print("Try" + "\r\n");
//            out.flush();
//            System.out.println("Message sent");
//            Thread.sleep(1000);
//        }
//    }
//}