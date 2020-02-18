import socket
import sys

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432        # The port used by the server

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
socket.bind((host, port))   # Bind to port
socket.listen(1)            # Wait for client connection


while True:
    print("1")
    # Establish connection with client
    connection, address = socket.accept()
    print("Connected with client -", address)

    while True:
        print("2")
        # Receive Command from client
        command = connection.recv(1024)
        print("Command received: ", command.decode('UTF-8'))

        if (command.decode('UTF-8') == 'QUIT'):
            print("3")
            print("See you again client -", address)
            connection.close()
            break
        else:
            # Tokenize command and save filename
            commands = command.decode().split(' ', 1)
            file = commands[1]

            # Receive incoming data, write to file and upload file to the server
            if (commands[0] == 'UPLD'):
                print("4")
                with open(file, 'w') as writefile:
                    while True:
                        print("5")
                        data = connection.recv(1024)
                        # if data is empty
                        if not data:
                            break
                        writefile.write(data.decode('UTF-8'))
                        writefile.close()
                        print("5.1")
                        break

            # Send all data from file to client to download
            elif (commands[0] == 'DWLD'):
                print("6")
                with open(file, 'r') as readfile:
                    for data in readfile:
                        connection.sendall(data.encode('UTF-8'))
            print("7")

    break

socket.close()
