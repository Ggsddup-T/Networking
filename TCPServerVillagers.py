from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
counter = 0
while counter < 3:
     connectionSocket, addr = serverSocket.accept()
     connectionSocket.settimeout(10)
     try:
          wolf_location = connectionSocket.recv(1024).decode()
          send_hunter(wolf_location) # a villager function
          connectionSocket.send('hunter sent')
     except timeout:
          counter += 1
     connectionSocket.close()
