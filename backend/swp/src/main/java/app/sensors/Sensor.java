package app.sensors;

import java.time.LocalDateTime;

public abstract class Sensor<T> implements Measurable {

    private Integer id;
    private LocalDateTime measurementTime;
    private T measurementValue;

}
