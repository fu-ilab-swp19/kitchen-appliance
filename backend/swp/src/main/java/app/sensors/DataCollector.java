package app.sensors;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

@Component
public class DataCollector {

    @Scheduled(fixedRate = 5000)
    public void executeTask() {
//        for (Sensor s : SensorCollection.getCollection().getSensors()) {
//            s.getParamValue();
//        }

        Socket socket = null;
        try {
            socket = new Socket("127.0.0.1", 60563);
        } catch (IOException e) {
            e.printStackTrace();
        }
        BufferedReader stdIn = null;
        try {
            stdIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        } catch (IOException e) {
            e.printStackTrace();
        }
        PrintWriter out = null;
        try {
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Trying to read...");
        String in = null;
        try {
            in = stdIn.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(in);
        out.print("Try" + "\r\n");
        out.flush();
        System.out.println("Message sent");
    }
}
