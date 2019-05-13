package app.sensors;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class DataCollector {

    @Scheduled(fixedRate = 10000)
    public void executeTask() {
        for (Sensor s : SensorCollection.getCollection().getSensors()) {
            s.getParamValue();
        }

    }
}
