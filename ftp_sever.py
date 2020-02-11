import socket
import sys

host = "127.0.0.1"
port = 65432

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(1)
while True:
    connection, address = socket.accept()
    command = connection.recv(1024)
    if (command == 'quit'):
        break
    else:
        commands = command.split(' ', 1)
        file = commands[1]
        if (commands[0] == 'UPLD'):
            with open(file, 'wb') as writefile:
                while True:
                    data = connection.recv(1024)
                    #if data empty
                    if not data:
                        break
                    writefile.write(data)
                    writefile.close()
                    break
        elif (commands[0] == 'DWLD'):
            with open(file, 'rb') as getfile:
                for data in getfile:
                    connection.sendall(data)
    connection.close()
socket.close()
