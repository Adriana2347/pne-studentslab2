import socket
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080

def process_client(cs):
    # -- Receive the request message
    req_raw = cs.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")


    lines = req.split('\n')
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    path_req = req_line.split(" ")[1]
    path_req_name = path_req.strip("/")
    termcolor.cprint(path_req_name, "green")

    try:
        if path_req_name == "info/A":
            with open("html/info/A.html", "r", encoding="utf-8") as f:
                body = f.read()
        elif path_req_name == "info/C":
            with open("html/info/C.html", "r", encoding="utf-8") as f:
                body = f.read()
    except FileNotFoundError:
        body = "<h1>404 Not Found</h1><p>The requested page was not found.</p>"


    status_line = "HTTP/1.1 404 ok\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body

    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: Avoid "Port already in use" error
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Bind to IP and PORT
ls.bind((IP, PORT))

# -- Start listening
ls.listen()

print("pink server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        cs, client_ip_port = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        # -- Service the client
        process_client(cs)

        # -- Close the client socket
        cs.close()