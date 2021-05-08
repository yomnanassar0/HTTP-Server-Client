serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = "127.0.0.1"
serverPort = 12345
print(f"Server IP: {serverIP} , Server Port: {serverPort}")
serverSocket.bind((serverIP,serverPort))
serverSocket.listen(1)
while True:
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f"A client with address : {addr} has just connected")
    try:
        message = connectionSocket.recv(2048)
        print(message.decode())
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
       
        header = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(header.encode())
       
        connectionSocket.close()

    #serverSocket.close()