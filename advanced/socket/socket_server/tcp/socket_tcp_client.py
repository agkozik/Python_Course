import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

sock.send(b'Message from Client')
print('Send csv_data to Server.')
result = sock.recv(64)
print('Response from Server: ', result)
sock.close()
