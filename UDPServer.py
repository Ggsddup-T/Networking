from socket import *  # import socket names (socket, AF_INET, SOCK_DGRAM, etc.)

serverPort = 12000  # port this server will listen on

serverSocket = socket(AF_INET, SOCK_DGRAM)  # create a UDP socket (IPv4, datagram)
serverSocket.bind(('127.0.0.1', serverPort))  # bind to localhost and port 12000

print("UDP server is ready!")  # show that the server is waiting for packets

while True:  # loop forever so many clients can be served
    message, clientAddress = serverSocket.recvfrom(2048)  # wait for a UDP packet and the sender's address

    print("Received:", message.decode())  # print the received bytes as text

    modifiedMessage = message.decode().upper()  # convert the message to uppercase

    serverSocket.sendto(  # send a UDP packet back to the client
        modifiedMessage.encode(),  # convert the uppercase string to bytes
        clientAddress  # send to the address the packet came from
    )
