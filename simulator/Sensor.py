import numpy as np
import time
from threading import Thread

from SensorThread import SensorThread
from SensorServer import SensorServer

class Sensor():
	
	def __init__(self, id, description, update_interval):
		
		self.id = id
		self.description = description
		self.update_interval = update_interval
		self.value = None
		
		SensorThread(self)
		
		SensorServer(self)
		
	def update(self):
		
		raise NotImplementedError('Should have implemented this')
		
	def randomFromTupel(self, tupel):
		
		_min, _max, mu, sd = tupel
		return min(_max, max(_min, np.random.normal(mu, sd, 1)[0]))