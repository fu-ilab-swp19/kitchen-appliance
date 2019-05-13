package app.database;

import javax.persistence.*;
import java.io.Serializable;
import java.time.LocalDateTime;

@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "type")
@Table(name = "measurements")
public abstract class Measurement implements Serializable {

    @Id
    @Column(name="id", updatable = false, nullable = false)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer sensorId;

    @Column(name = "msr_time", nullable = false, updatable = false)
    private LocalDateTime measuredAt;

}
