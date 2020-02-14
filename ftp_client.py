import socket
import sys
import os
import struct

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server
BUFFER = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conn():
    s.connect((HOST, PORT))
    print("You have been connected")

def upload(fullcommand):
    s.send(fullcommand.encode('utf-8'))
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    with open(file, 'rb') as infile:
        for data in infile:
            s.sendall(data)
    infile.close()
    print("File uploaded")

def givelist():
    print("Here is your list")

def download(fullcommand):
    s.send(fullcommand.encode('utf-8'))
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    with open(file, 'wb') as outfile:
        while True:
            data = s.recv(1024)
            if not data:
                break
            outfile.write(data)
            print("loop2")
        outfile.close()
    print("File downloaded")

def discon(fullcommand):
    s.send(fullcommand.encode())
    s.close()
    print("Disonnected")

while True:
    str = input("Command?:\n")
    commands = str.split(' ', 1)
    if commands[0] == "QUIT":
        print("Goodbye")
        discon(str)
        quit()
        break
    elif commands[0] == "CONN":
        conn()
    elif commands[0] == "UPLD":
        upload(str)
        print("UPPPPP")
    elif commands[0] == "LIST":
        givelist()
    elif commands[0] == "DWLD":
        download(str)
        print("DOWNNNNNN")
    else:
        print("INVALID COMMAND")
