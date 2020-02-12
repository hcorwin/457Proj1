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
    command.decode('utf-8')
    if (command == 'quit'):
        break
    else:
        commands = command.decode().split(' ', 1)
        file = commands[1]
        if (commands[0] == 'UPLD'):
            with open(file, 'w') as writefile:
                while True:
                    data = connection.recv(1024)
                    #if data empty
                    if not data:
                        break
                    writefile.write(data.decode('utf-8'))
                    writefile.close()
                    break
        elif (commands[0] == 'DWLD'):
            with open(file, 'r') as getfile:
                for data in getfile:
                    connection.sendall(data.encode('utf-8'))
    connection.close()
socket.close()
