import base64

# file = open("encodedflag.txt", "rb")
# for line in file:
# 	encoded = line
# print(encoded)
# decoded = encoded
# for i in range(5):
# 	decoded = base64.b16decode(decoded)
# for i in range(5):
# 	decoded = base64.b32decode(decoded)
# for i in range(5):
# 	decoded = base64.b64decode(decoded)
# print(decoded)

# file = open("b64.txt", "rb")
#
# for line in file:
# 	encoded = line
# print(encoded)
#
# for i in range(50):
# 	encoded = base64.b64decode(encoded)
#
# print(encoded)

import socket
from time import sleep

host='10.10.119.125'
port = 3010
number = 0.0



while (port == 3010):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
		s.send(request.encode())
		data = repr(s.recv(4096))
		s.close()
		data = data[-22:-17]
		port = int(data.replace(":", ""))
		s.close()
	except:
		s.close()
		pass
print(port)

old_port = port
while (port != 9765):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print(str(port) + " <--- port" )
		print(str(old_port) + " <--- old_port" )
		s.connect((host, port))
		print(1)
		
		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
		print(2)
		s.send(request.encode())
		print(3)
		data = repr(s.recv(4096)).split("\\r\\n")[-1].replace("'", "").split(" ")
		
		print(data + " <---data")
		operation = data[0]
		nextNumber = float(data[1])
		port = int(data[2])
		

		if(old_port == port):
			print("wait")
			sleep(2)
		else:
			old_port = port
			if(operation == 'add'):
				number += float(nextNumber)
			elif(operation == 'minus'):
				number -= float(nextNumber)
			elif(operation == 'multiply'):
				number *= float(nextNumber)
			elif(operation == 'divide'):
				number /= float(nextNumber)
		s.close()
	except:
		sleep(2)
		# print(ValueError)
		s.close()
		pass
		
		
	
	
	
	

	# while(port != 9765):
	# 	s.connect((host, port))
	# 	request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
	# 	print(request)
	# 	s.send(request.encode())
	#
	# 	data = repr(s.recv(4096))
	# 	print(data)
	#
	# 	print(data)
	# print(data[int(data.index("onPort")) + 7: int(data.index("onPort")) + 4])

# :1337"<

# host='10.10.151.69'
# port = 3010
# number = 0

# while 1:
# 	try:
# 		s = socket.socket()
# 		s.connect((host,port))
# 		if (port == 9765):
# 			break
# 		old_port = port
# 		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
# 		s.send(request.encode())
# 		response = s.recv(4096)
# 		http_response = repr(response)
# 		http_trim = http_response[167:]
# 		http_trim = http_trim.replace('\'','')
# 		data_list = list(http_trim.split(" "))
# 		port = int(data_list[2])
# 		print('Operation: '+data_list[0]+', number: '+ data_list[1]+', next port: '+ data_list[2])
# 		if(port != old_port):
# 			if(data_list[0] == 'add'):
# 				number += float(data_list[1])
# 			elif(data_list[0] == 'minus'):
# 				number -= float(data_list[1])
# 			elif(data_list[0] == 'multiply'):
# 				number *= float(data_list[1])
# 			elif(data_list[0] == 'divide'):
# 				number /= float(data_list[1])
# 		s.close()
# 	except:
# 		s.close()
# 		pass

# print(number)
