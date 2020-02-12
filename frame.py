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
    with open(file, 'r') as infile:
        for data in infile:
            s.sendall(data.encode('utf-8'))
    print("File uploaded")
    return

def givelist():
    print("Here is your list")

def download(fullcommand):
    s.send(fullcommand.encode('utf-8'))
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    with open(file, 'w') as outfile:
        while True:
            data = s.recv(1024)
            if not data:
                break
            outfile.write(data.decode('utf-8'))
        outfile.close()
    print("File downloaded")
    return

def discon():
    s.close()
    print("Disonnected")

while True:
    str = input("Command?:\n")
    commands = str.split(' ', 1)
    if commands[0] == "QUIT":
        print("Goodbye")
        discon()
        quit()
        break
    elif commands[0] == "CONN":
        conn()
    elif commands[0] == "UPLD":
        upload(str)
    elif commands[0] == "LIST":
        givelist()
    elif commands[0] == "DWLD":
        download(str)
    else:
        print("INVALID COMMAND")
