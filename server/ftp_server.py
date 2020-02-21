import socket
import sys
import os

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432  # The port used by the server

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
socket.bind((host, port))  # Bind to port
socket.listen(1)  # Wait for client connection

while True:
    # Establish connection with client
    connection, address = socket.accept()
    print("Connected with client -", address)

    while True:
        # Receive Command from client
        command = connection.recv(1024)
        print("Command received: ", command.decode('UTF-8'))

        if (command.decode('UTF-8') == 'QUIT'):
            print("See you again client -", address)
            connection.close()
            break
            # Send list of files in the server
        elif (command.decode('UTF-8') == 'HMANY'):
            data = os.listdir()
            count = 0
            for line in data:
                count += 1
            connection.send(str(count).encode('UTF-8'))
        elif (command.decode('UTF-8') == 'LIST'):
            data = os.listdir()
            print("Sending directory list:")
            for line in data:
                print(">", line)
                connection.send(line.encode('UTF-8'))
                #connection.send(' '.encode('UTF-8'))
        else:
            # Tokenize command and save filename
            commands = command.decode().split(' ', 1)
            file = commands[1]
            print(file)

            # Receive incoming data, write to file and upload file to the server
            if (commands[0] == 'UPLD'):
                with open(file, 'w') as writefile:
                    while True:
                        data = connection.recv(1024)
                        # if data is empty
                        if not data:
                            break
                        writefile.write(data.decode('UTF-8'))
                        writefile.close()
                        print(data)
                        break

            # Send all data from file to client to download
            elif (commands[0] == 'DWLD'):
                data = os.listdir()
                if file in data:
                    with open(file, 'r') as readfile:
                        for data in readfile:
                            connection.sendall(data.encode('UTF-8'))
                else:
                    print("File not found")
                    connection.send("no".encode('UTF-8'))

    break

socket.close()

