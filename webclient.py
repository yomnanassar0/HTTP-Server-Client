from socket import *
serverIP = "127.0.0.1"
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))


req = "GET /" + "hello.html" + " HTTP/1.1\r\n\r\n"
clientSocket.send(req.encode())

rec=""
rec2 = clientSocket.recv(1024).decode()
while True:

    if len(rec2) != 0:
        rec2 = clientSocket.recv(1024).decode()
        rec += rec2
    else:
        break

print(rec)


print("socket's closing")
clientSocket.close()