import socketserver
import socket
from threading import Thread

from SensorServerHandler import SensorServerHandler

class V6Server(socketserver.TCPServer):
    address_family = socket.AF_INET

class SensorServer():

	def __init__(self, sensor):
		
		t = Thread(target = self.asynch_execution, args = [sensor])
		
		t.start()
		
	def asynch_execution(self, sensor):
		
		HOST = '127.0.0.1'
		PORT = 0
		
		server = V6Server((HOST, PORT), SensorServerHandler)
		
		port = server.server_address[1]
		print('sensor server for id', sensor.id, 'listens to port', port)
		
		server.sensor = sensor
		
		server.serve_forever()