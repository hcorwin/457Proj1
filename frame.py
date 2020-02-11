import socket
import sys
import os
import struct

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def connect():
    print("You have been connected")

def disconnect():
    print("You have been disconnected")

def givelist():
    print("Here is your list")

def download():
    print("What would you like to download?")

def delete():
    print("What would you like to delete?")

while True:
    str = input("Command?:\n")
    if str.upper() == "QUIT":
        print("Goodbye")
        quit()
        break
    elif str.upper() == "CONN":
        connect()
    elif str.upper() == "DISC":
        disconnect()
    elif str.upper() == "LIST":
        givelist()
    elif str.upper() == "DWLD":
        download()
    elif str.upper() == "DELE":
        delete()
    else:
        print("INVALID COMMAND")