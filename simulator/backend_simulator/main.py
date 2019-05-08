import socket
import sys

def main():
	
	HOST = '::1'
	PORT = int(sys.argv[1])
	
	sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	
	try: 
		sock.connect((HOST, PORT))
		sock.sendall(bytes('TEST\n', 'utf-8'))
		
		received = str(sock.recv(1024), 'utf-8')
	finally:
		sock.close()
		
	print('received:', received)
	
if __name__ == "__main__":
	
    main()