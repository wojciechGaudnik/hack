import socket
import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
	Cipher, algorithms, modes
)


host = "10.10.63.203"
port = 4000
byte_message = bytes("hello\n", "utf-8")


def AES_GCM_decrypt(key, iv, ciphertext, tag):
	associated_data = ''
	decryptor = Cipher(algorithms.AES(key), modes.GCM(iv,tag, 4), backend=default_backend()).decryptor()
	decryptor.authenticate_additional_data(associated_data)
	return decryptor.update(ciphertext) + decryptor.finalize()

def SHA256_hash(hash_string):
	sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature


print("start")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(byte_message, (host, port))
data = s.recv(2048)
print(data)

s.sendto(b'ready', (host, port))
data = s.recv(2048)
checksum = str(data[104:136])
hex_checksum = checksum.encode()
print(data)
print(checksum)
print(hex_checksum)

while 1:
	s.sendto(b'final\n', (host, port))
	flag = s.recv(2048)
	
	s.sendto(b'final\n', (host, port))
	tag = s.recv(2048)
	
	key = b'thisisaverysecretkeyl337'
	iv = b'secureivl337'
	tag = bytes(tag)
	cipherText = bytes(flag)
	plainText = AES_GCM_decrypt(key, iv, cipherText, tag)
	
	hash_string = SHA256_hash(plainText)
	if(hash_string == hex_checksum):
		print('flag is: ' + plainText)
		break


