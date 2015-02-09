__author__ = 'Teddy'

import socket
import sys

from server import port


host = socket.gethostname()

def Main():
    sock = socket.socket()

    try:
        print("attempting connection to server\n...")
        sock.connect((host, port))
        print("connection to server successful")

        msg = sock.recv(1024)
        print("server says: " + bytes.decode(msg) + "\n")

        request = ' '.join(sys.argv[1:len(sys.argv)])

        sock.send(str.encode(request))

        response = sock.recv(1024)

        response = bytes.decode(response)

        if response.startswith('P'):
            response = 'P{:.2f}'.format(float(response[1:len(response)]))

        print("request result: " + response + "\n")

        sock.close()

    except ConnectionResetError:
        print("\n+--connection to server lost--+")
        quit()

    except ConnectionAbortedError:
            print("\n+--connection to server lost--+")
            quit()

    except ConnectionRefusedError:
        print("\n+--could not connect to server--+")
        quit()


if __name__ == "__main__":
    Main()
