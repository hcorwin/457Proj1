import socket
import sys
import os
import struct

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object


def connect():
    # Socket connects to server
    s.connect((HOST, PORT))
    print(f"+ Connected to server - {HOST}:{PORT}")


def disconnect(command):
    print("Goodbye server!")

    # Socket sends encoded command to server
    s.send(command.encode('UTF-8'))

    # Socket disconnects from server
    s.close()

    print("\n+ Disonnected")


def upload(fullcommand):
    # Socket sends encoded command to server
    s.send(fullcommand.encode('UTF-8'))

    # Tokenize command and save filename
    commands = fullcommand.split(' ', 1)
    file = commands[1]

    # Send all data from file to server to upload
    with open(file, 'r') as infile:
        for data in infile:
            s.sendall(data.encode('UTF-8'))

    print("Successfully uploaded file:", file)
    return


def download(fullcommand):
    # Socket sends encoded command to server
    s.send(fullcommand.encode('UTF-8'))

    # Tokenize command and save filename
    commands = fullcommand.split(' ', 1)
    file = commands[1]

    # Receive incoming data, write to file and download file to client
    with open(file, 'w') as outfile:
        while True:
            data = s.recv(1024)
            # if data is empty
            if not data:
                break
            outfile.write(data.decode('UTF-8'))
            outfile.close()
            print("Successfully downloaded file:", file)
            break
    return


def getlist(command):
    # Socket sends encoded command to server
    s.send(command.encode('UTF-8'))

    # Receive list of files in the server
    data = s.recv(1024)
    dirlist = data.decode('UTF-8').split(' ')

    # Print out the list of files
    print("Server directory:")
    for filename in dirlist:
        print(">", filename)


while True:
    str = input("\n+ COMMAND: ")
    commands = str.split(' ', 1)

    if commands[0] == "QUIT":
        disconnect(str)
        quit()
        break
    elif commands[0] == "CONNECT":
        connect()
    elif commands[0] == "STORE":
        upload(str)
    elif commands[0] == "LIST":
        getlist(str)
    elif commands[0] == "RETRIEVE":
        download(str)
    else:
        print("+ INVALID COMMAND")

