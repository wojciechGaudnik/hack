import socket
import sys
import time

host="10.10.119.125"
port = 1337
number = 0

while 1:
	try:
		s = socket.socket()
		s.connect((host,port))
		if (port == 9765):
			break
		old_port = port
		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
		s.send(request.encode())
		response = s.recv(4096)
		http_response = repr(response)
		http_trim = http_response[167:]
		http_trim = http_trim.replace('\'','')
		data_list = list(http_trim.split(" "))
		port = int(data_list[2])
		print('Operation: '+data_list[0]+', number: '+ data_list[1]+', next port: '+ data_list[2])
		if(port != old_port):
			if(data_list[0] == 'nadd'):
				number += float(data_list[1])
			elif(data_list[0] == 'nminus'):
				number -= float(data_list[1])
			elif(data_list[0] == 'nmultiply'):
				number *= float(data_list[1])
			elif(data_list[0] == 'ndivide'):
				number /= float(data_list[1])
		print(number)
		s.close()
	except:
		s.close()
		pass

print(number)