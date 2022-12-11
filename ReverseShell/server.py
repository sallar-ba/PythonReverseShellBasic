# Hacker/User Computer

# Two Computer Can Connect To Each other
import socket
# Terminal Command in Python
import sys


# Create a Socket (connect to computers)
def createSocket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket() # Creating a Socket
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

# Binding the Socket and Listening for Connections
def bindSocket():
    try:
        global host
        global port
        global s

        print("Binding Port: " + str(port))

        s.bind((host, port)) # Tuple in Python
        s.listen(5) # Atmost 5 connections

    except socket.error as msg:
        print("Socket Binding Error: " + str(msg) + "\n" + "Retrying...")
        bindSocket() # Recursively Calling Again

# Accepting Connection With Client (Sockets Must Be Listening)
def acceptSocket():
    connection, address = s.accept()
    print("Connection Established With: IP " + address[0] + ", Port: " + str(address[1]))

    connection.close()