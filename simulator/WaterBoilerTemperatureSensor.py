import numpy as np
from Sensor import Sensor
from const import AMBIENT_TEMPERATURE, WATER_BOILER_DURATION, WATER_BOILER_DOWNTIME, WATER_BOILER_FIRST_ACTIVE, WATER_BOILER_ERROR, WATER_BOILER_COOLDOWN

class WaterBoilerTemperatureSensor(Sensor):

	def __init__(self, id, description, update_interval):
		
		self.ambient = self.randomFromTupel(AMBIENT_TEMPERATURE)
		
		self.time = None
		self.time_last_active = None
		self.time_next_active = self.randomFromTupel(WATER_BOILER_FIRST_ACTIVE)
		self.time_last_cooldown = None
		self.active = False
		self.active_step = None
		self.active_begin = None
		self.cooldown = False
		self.cooldown_step = None
		self.cooldown_begin = None
		
		Sensor.__init__(self, id, description, update_interval)
		
	def update(self):
		
		if self.time is None:
			self.time = 0
		else:
			self.time += self.update_interval
			
		error = self.randomFromTupel(WATER_BOILER_ERROR)
		
		if self.active:
			active_time_spent = self.time - self.time_last_active
			real = self.active_begin + self.active_step * active_time_spent
			if real > 100:
				self.active = False
				self.time_next_active = self.randomFromTupel(WATER_BOILER_DOWNTIME)
				self.cooldown = True
				self.time_last_cooldown = self.time
				self.cooldown_begin = self.value
				cooldown = self.randomFromTupel(WATER_BOILER_COOLDOWN)
				self.cooldown_step = cooldown / self.update_interval
				self.value -= self.cooldown_step + error
			else:
				self.value = real + error
		elif self.cooldown:
			cooldown_time_spent = self.time - self.time_last_cooldown
			real = self.cooldown_begin - self.cooldown_step * cooldown_time_spent
			if real < self.ambient:
				self.cooldown = False
				self.value = self.ambient + error
			else:
				self.value = real + error
		else:
			if self.time > self.time_next_active:
				self.active = True
				self.time_last_active = self.time
				active = self.randomFromTupel(WATER_BOILER_DURATION)
				self.active_step = active / self.update_interval
				self.value += self.active_step + error
			else:
				self.value = self.ambient + error
		