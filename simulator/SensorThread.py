from threading import Thread
import time

import Sensor

class SensorThread(Thread):

	def __init__(self, sensor):
		
		Thread.__init__(self, target = self.loop, args = [sensor])
		
		self.start()
		
	def loop(self, sensor):
		
		while(True):
			sensor.update()
			print(sensor.id, sensor.value)
			time.sleep(0.1 * sensor.update_interval)