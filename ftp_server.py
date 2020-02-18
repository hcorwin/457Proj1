import socket
import sys

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432        # The port used by the server

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
socket.bind((host, port))   # Bind to port
socket.listen(1)            # Wait for client connection

while True:
    # Establish connection with client
    connection, address = socket.accept()
    print("Connected with client -", address)

    # Receive Command from client
    command = connection.recv(1024)
    print("Command received: ", (command.decode('UTF-8')))

    if (command.decode('UTF-8') == 'QUIT'):
        print("See you again client -", address)
        break
    else:
        # Tokenize command and save filename
        commands = command.decode().split(' ', 1)
        file = commands[1]

        if (commands[0] == 'UPLD'):
            with open(file, 'w') as writefile:
                while True:
                    data = connection.recv(1024)
                    print("Data=%s", (data))
                    #if data empty
                    if not data:
                        break
                    writefile.write(data.decode('UTF-8'))
                    writefile.close()
                    break
        elif (commands[0] == 'DWLD'):
            with open(file, 'r') as getfile:
                for data in getfile:
                    connection.sendall(data.encode('UTF-8'))

    connection.close()
socket.close()
