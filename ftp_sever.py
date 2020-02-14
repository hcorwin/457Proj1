import socket
import sys

host = "127.0.0.1"
port = 65432

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(5)
while True:
    print("am i getting hit")
    connection, address = socket.accept()
    command = connection.recv(1024)
    print("where am i")
    if (command == 'QUIT'):
        print("quiting")
        connection.close()
        socket.close()
        break
    else:
        commands = command.decode().split(' ', 1)
        print(commands[0] + " 1 " + commands[1])
        file = commands[1]
        print("what the")
        if (commands[0] == 'UPLD'):
            with open(file, 'wb') as writefile:
                print("loop3")
                while True:
                    data = connection.recv(1024).decode()
                    print(data + "***")
                    #if data empty
                    if not data:
                        break
                    writefile.write(data.encode())
            writefile.close()
        elif (commands[0] == 'DWLD'):
            print("?")
            with open(file, 'rb') as getfile:
                for data in getfile:
                    print("loop4")
                    connection.sendall(data)
            getfile.close()
