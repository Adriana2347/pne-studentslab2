import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.103"# the IP address depends on the machine running the server

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #SI YA LO ESTA USANDO Q no salte error y lo vuelva a usar

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")

# -- Waits for a client to connect

while True:
    print("Waiting for Clients to connect")
    (client_socket, client_addr) = ls.accept()
    print("A client has connected to the server!")

    msg_raw = client_socket.recv(2048)
    print("Recived!", msg_raw.decode())

    client_socket.send("Hello! Im the happy server.".encode())
    client_socket.close()
    # -- Close the socket
    ls.close()
