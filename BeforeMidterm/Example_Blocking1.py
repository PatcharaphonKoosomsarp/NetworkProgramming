import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

prot = 1234 if len(sys.argv) < 2 else int(sys.argv[1])
sock.bind(('localhost', prot))
sock.listen(5)

try:
    while True:
        conn, addr = sock.accept()
        
        data = conn.recv(1024)
        while data:
            print(data)
            data = conn.recv(1024)
except KeyboardInterrupt:
    sock.close