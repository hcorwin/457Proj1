import socket
import sys
import os
import struct

BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

def conn(fullcommand):
    # Tokenize command and save filename
    commands = fullcommand.split(' ')

    # Input server's hostname or IP address
    HOST = commands[1]
    # Input port number used by the server
    PORT = int(commands[2])

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
    # Tokenize command and save filename
    commands = fullcommand.split(' ', 1)
    file = commands[1]
    dirlist = os.listdir()

    if file in dirlist:
        # Socket sends encoded command to server
        s.send(fullcommand.encode('UTF-8'))

        # Send all data from file to server to upload
        with open(file, 'r') as infile:
            for data in infile:
                print("Uploading a file...")
                s.sendall(data.encode('UTF-8'))
                print("Successfully uploaded file:", file)
    else:
        print("File not found")
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
                print("Downloading a file...")
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


    if commands[0] == "QUIT" and len(commands) == 1:
        try:
            discon(str)
            quit()
            break
        except:
            quit()
    elif commands[0] == "CONN" and len(commands) > 1:
        try:
            conn(str)
        except:
            print("Server Down")
    elif commands[0] == "UPLD" and len(commands) > 1:
        try:
            upload(str)
        except:
            print("Not connected")
    elif commands[0] == "LIST" and len(commands) == 1:
        try:
            givelist(str)
        except:
            print("Not connected")
    elif commands[0] == "DWLD" and len(commands) > 1:
        try:
            download(str)
        except:
            print("Not connected")
    else:
        print("INVALID COMMAND")

