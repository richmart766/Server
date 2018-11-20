

def usage( script_name ):
    print( 'Usage: py ' + script_name + ' <port number>' )

def	cthreas(soc,adr):
	test = 0
	while True:
		try:
			msg = soc.recv(1024)
			if msg:
				if test ==0:
					name = msg.decode().rstrip()
					test +=1
				else:
					sender = name + ": " + msg.decode()
					threading.Thread(target = sending, args = (sender,soc)).start()
			else:
				remove(soc)
		except:
			remove(soc)
			return

def sending(mess,soc):
	for connects in list_connect:
		if connects != soc:
			try:
				connects.send(mess.encode())
			except:
				connects.close()
				remove(connects)
			
def remove(connection):
		if connection in list_connect:
			list_connect.remove(connection)

list_connect = []
	
if __name__ == "__main__":
	import sys, time
	import socket
	import threading
	argc= len( sys.argv )
	if argc != 2 :
		usage( sys.argv[0] )
		sys.exit()
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversocket.bind(('', 6001))
	serversocket.listen(50)
	while True:
		sock, addr= serversocket.accept()
		list_connect.append(sock)
		threading.Thread(target = cthreas, args = (sock,addr)).start()
	
	sock.close() 
	serversocket.close()
