# Unix Socket (when using file instead of host)
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Test Message', 'unix_sock')