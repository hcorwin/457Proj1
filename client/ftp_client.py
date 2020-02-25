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
    print(f"Connected to server - ({HOST}, {PORT})")

def discon(command):
    # Socket sends encoded command to server
    s.send(command.encode('UTF-8'))

    print("Goodbye server!")
    print("Disonnected")

    # Socket disconnects from server
    s.close()

def upload(fullcommand):
    # Socket sends encoded command to server
    s.send(fullcommand.encode('UTF-8'))

    # Tokenize command and save filename
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    dirlist = os.listdir()

    if file in dirlist:
        # Send all data from file to server to upload
        with open(file, 'r') as infile:
            for data in infile:
                s.sendall(data.encode('UTF-8'))

        print("Successfully uploaded file:", file)
    else:
        print("File not found")
        s.send("no".encode('UTF-8'))
    return

def download(fullcommand):
    # Socket sends encoded command to server
    s.send(fullcommand.encode('UTF-8'))

    # Tokenize command and save filename
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    string = ''

    # Receive incoming data, write to file and download file to client
    with open(file, 'w') as outfile:
        while True:
            data = s.recv(1024)
            # if data is empty
            if not data:
                break
            if data.decode('UTF-8') == 'no':
                print("File not found!")
                string = 'remove'
                break
            else:
                outfile.write(data.decode('UTF-8'))
                outfile.close()
                print("Successfully downloaded file:", file)
                break
    if string == 'remove':
        os.remove(file)
    return

def givelist(fullcommand):
        # Socket sends encoded command to server
        s.send(fullcommand.encode('UTF-8'))

        # Receive list of files in the server
        data = s.recv(1024)
        dirlist = data.decode('UTF-8').split(' ')

        # Print out the list of files
        for filename in dirlist:
            print(">", filename)


while True:
    str = input("\nCommand? ")
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
        givelist(str)
    elif commands[0] == "DWLD":
        download(str)
    else:
        print("INVALID COMMAND")

