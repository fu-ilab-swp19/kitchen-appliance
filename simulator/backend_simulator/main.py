import socket
import sys
import matplotlib.pyplot as plt
import time
import numpy as np
import datetime

def getSensorData(host, port):
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	received = None
	
	try: 
		sock.connect((host, port))

		print("Connected to host {} and port {}".format(host,port))
		sock.sendall(bytes('\n', 'utf-8'))
		
		received = float(str(sock.recv(1024), 'utf-8'))
	finally:
		sock.close()
		
	if received is None:
		raise
	
	return received

def main():
	
	host = '127.0.0.1'
	port = int(sys.argv[1])
	
	update_interval = float(sys.argv[2])
	
	x_data = np.array([])
	x_ctr = 0
	y_data = np.array([])
	
	fig = plt.figure(figsize=(13,6))
	ax = fig.add_subplot(111)
	ax.plot(x_data, y_data)
	
	while(True):
		try:
			d = getSensorData(host, port)
			print(d)
			#y_data = np.append(y_data, d)[-500:]
			#x_data = np.append(x_data, datetime.datetime.now())[-500:]
			#ax.clear()
			#ax.plot(x_data,y_data)
			#plt.pause(0.1)
		except:
			pass
		time.sleep(update_interval)
	
if __name__ == "__main__":
	
    main()