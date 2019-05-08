from WaterBoilerTemperatureSensor import WaterBoilerTemperatureSensor

def main():
	
	water_boiler_1 = WaterBoilerTemperatureSensor(1, 'first sensor.', 2)
	water_boiler_2 = WaterBoilerTemperatureSensor(2, 'second one.', 3)

if __name__ == "__main__":
	
    main()