

def usage( script_name ):
    print( 'Usage: py ' + script_name + ' <port number>')

def receive():
	try:
		msg_bytes = sock.recv(1024)
	except:
		msg_bytes = False
	while msg_bytes:
		answer = msg_bytes.decode()
		print(answer, end = '')
		try:
			msg_bytes= sock.recv(1024)
		except:
			break
	sock.close()
	os._exit(0)	
	
def send():
	msg_bytes= "hello"
	msg_bytes = sys.stdin.readline()
	sock.send((msg_bytes).encode())
	time.sleep( 1 )
	while msg_bytes:	
		print("Enter an option ('m', 'f', 'x'):")
		print('  (M)essage (send)')
		print('  (F)ile (request)')
		print(' e(X)it')
		msg_bytes = sys.stdin.readline().rstrip( '\n' )
		if(msg_bytes == "m"):
			print("Enter your message:")
			msg_bytes = sys.stdin.readline()
			sock.send((msg_bytes).encode())
		if(msg_bytes == "f"):
			print("who owns the file?")
			msg_bytes = sys.stdin.readline()
			print("Which file do you want")
			msg_bytes = sys.stdin.readline()
		if(msg_bytes == "x"):
			sock.close()
			os._exit(0)
			return
		
if __name__ == "__main__":
	import sys, time
	import socket
	import threading
	import os
	argc= len( sys.argv )
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server= 'localhost'
	sock.connect((server, 6001))
	
	thread_c = threading.Thread(target = send)
	thread_c.start()
	thread_d = threading.Thread(target = receive)
	thread_d.start()
	thread_c.join()
	
	sock.close()
	os._exit(0)	
	sock.close()
