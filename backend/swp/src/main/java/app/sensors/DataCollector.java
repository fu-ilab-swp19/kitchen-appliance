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
    public void executeTask() throws IOException {

        Socket socket = new Socket("127.0.0.1", 60563);
        BufferedReader reader = null;
        reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        System.out.println("Trying to read data from a sensor.");
        String readData = reader.readLine();
        System.out.println("Read value: " + readData);
        out.flush();

    }
}
