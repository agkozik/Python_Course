# with operator
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: # UDP
    sock.bind(('127.0.0.1', 8888))
    print('8888 is binded')

    while True:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))