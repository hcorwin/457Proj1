import socket
import sys
import os
import struct

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server
BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

def conn():
    # Socket connects to server
    s.connect((HOST, PORT))
    print("Connected to server - (",HOST,",",PORT,")")

def discon(command):
    print("Goodbye server!")
    print("Disonnected")

    # Socket sends encoded command to server
    s.send(command.encode('UTF-8'))

    # Socket disconnects from server
    s.close()

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
    return

def givelist():
    print("Here is your list:")


while True:
    str = input("Command? ")
    commands = str.split(' ', 1)

    if commands[0] == "QUIT":
        discon(str)
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
