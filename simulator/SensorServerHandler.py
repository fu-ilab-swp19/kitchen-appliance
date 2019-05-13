import socketserver

class SensorServerHandler(socketserver.BaseRequestHandler):
	
	def handle(self):
		
		self.request.sendall(bytes(str(self.server.sensor.value) + '\n', 'utf-8'))