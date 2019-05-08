import socketserver

class SensorServerHandler(socketserver.StreamRequestHandler):
	
	def handle(self):
		
		print('sensor server handler got a request. sensor id:', self.server.sensor.id)
		
		self.data = self.rfile.readline().strip()
		print("{} wrote:".format(self.client_address[0]))
		print(self.data)
		
		self.wfile.write(self.data.upper())