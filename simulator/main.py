from WaterBoilerTemperatureSensor import WaterBoilerTemperatureSensor
from threading import Thread

def updateSensor(sensor):
	while(True):
		sensor.update()
		print(sensor.id, sensor.value)

def main():
	water_boiler_1 = WaterBoilerTemperatureSensor(1, 'first sensor.', 2)
	water_boiler_2 = WaterBoilerTemperatureSensor(2, 'second one.', 3)
	
	t1 = Thread(target = updateSensor, args = [water_boiler_1])
	t2 = Thread(target = updateSensor, args = [water_boiler_2])
	t1.start()
	t2.start()

if __name__ == "__main__":
    main()