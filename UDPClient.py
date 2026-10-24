from socket import *  # import socket names (socket, AF_INET, SOCK_DGRAM, timeout, etc.)

serverName = '127.0.0.1'  # server IP (localhost = this same computer)
serverPort = 12000  # port the server is listening on

clientSocket = socket(AF_INET, SOCK_DGRAM)  # create a UDP socket (IPv4, datagram)
clientSocket.settimeout(5)  # wait at most 5 seconds for a reply

message = input("Enter a message: ")  # read a line of text from the keyboard

clientSocket.sendto(  # send a UDP packet to the server
    message.encode(),  # convert the string to bytes
    (serverName, serverPort)  # destination: server IP and port
)

try:  # try to receive a reply; may fail if the server is too slow
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # wait for a UDP packet (up to 2048 bytes)
    print("From server:", modifiedMessage.decode())  # print the reply as text
except timeout:  # runs if no packet arrives within 5 seconds
    print("No response received within 5 seconds.")  # tell the user there was no reply

clientSocket.close()  # close the socket
