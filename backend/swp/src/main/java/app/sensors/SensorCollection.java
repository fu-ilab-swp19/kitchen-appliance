package app.sensors;

import java.util.ArrayList;
import java.util.List;

public class SensorCollection {

    private static SensorCollection collection;
    private List<Sensor> sensors;

    private SensorCollection() {
        sensors = new ArrayList<>();
    }

    public static SensorCollection getCollection() {
        if (SensorCollection.collection == null) {
            SensorCollection.collection = new SensorCollection();
        }
        return SensorCollection.collection;
    }

    public List<Sensor> getSensors() {
        return this.sensors;
    }

    public void addSensor(Sensor s) {
        this.sensors.add(s);
    }

}
