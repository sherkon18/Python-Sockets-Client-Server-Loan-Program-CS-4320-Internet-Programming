import socket

host = 'Your PC IP address'
port = 12321


def main():
    sock = socket.socket()

    sock.bind((host, port))

    sock.listen(1)
    print("sever listening...")

    while True:
            (connection, address) = sock.accept()
            print("connection to client successful")
            
            sock.listen(1)
            print("\nwaiting for request...")
            request = connection.recv(1024)
            print(bytes.decode(request))

            print("Message from connected client: " + bytes.decode(request))
           
            connection.close()
            print("+--connection to client closed--+")        

if __name__ == "__main__":
    main()
