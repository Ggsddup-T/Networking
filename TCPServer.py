from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     # Handle one client at a time; accept() waits until a client connects.
     connectionSocket, addr = serverSocket.accept()
     print('Connected by', addr)
     # Read the client's message, uppercase it, and send the result back.
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.encode())
     # Close this client connection before accepting the next one.
     connectionSocket.close()

