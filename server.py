import socket
import os
import time
from time import sleep
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Waitiing for a Connection..")
print()
print("you have to wait for 3 seconds")
print()
sleep(3)
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode("Welcome to the Server\n"))
    while True:
        data = connection.recv(2048)
        print("client says: " + data.decode('utf-8'))
        reply=input("reply message from server ")
        if reply=='exit':
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print("Thread Number: " + str(ThreadCount))
    print("Welcome to the Server\n")

ServerSocket.close()
