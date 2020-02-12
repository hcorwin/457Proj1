import socket
import sys
import os
import struct

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
BUFFER = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def connect():
    s.connect(HOST, PORT)
    print("You have been connected")

def upload(fullcommand):
    s.send(fullcommand)
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    with open(file, 'rb') as infile:
        for data in infile:
            s.sendall(data)
    print("File uploaded")
    return

def givelist():
    print("Here is your list")

def download(fullcommand):
    s.send(fullcommand)
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    with open(file, 'wb') as outfile:
        while True:
            data = s.recv(1024)
            if not data:
                break
            outfile.write(data)
        outfile.close()
    print("File downloaded")
    return

while True:
    str = input("Command?:\n")
    if str.upper() == "QUIT":
        print("Goodbye")
        quit()
        break
    elif str.upper() == "CONN":
        connect()
    elif str.upper() == "UPLD":
        upload()
    elif str.upper() == "LIST":
        givelist()
    elif str.upper() == "DWLD":
        download()
    else:
        print("INVALID COMMAND")
