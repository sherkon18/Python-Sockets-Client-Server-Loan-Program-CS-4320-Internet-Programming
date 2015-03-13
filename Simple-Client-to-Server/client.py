import socket
import sys

host = 'Your PC IP address'
port = 12321

def Main():
    sock = socket.socket()
    sock.connect((host, port))
    sock.send(str.encode("hello"))
    
if __name__ == "__main__":
    Main()
