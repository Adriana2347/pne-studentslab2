import socket
from Seq1 import Seq


# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"# # the IP address depends on the machine running the server


# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #SI YA LO ESTA USANDO Q no salte error y lo vuelva a usar

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")


count = 0
new_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        # -- Close the listenning socket
        ls.close()
        # -- Exit!
        exit()
    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        msg_final = msg.strip().split(" ")

        if msg.strip() == "PING":
            print("PING COMMAND")
            response = "OK\n"
        else:
            response = " "
        print(response)


        seq_list = ["ACGT", "GGCT", "CAAT", "TCGA"]
        if msg_final[0] == "GET":
            print(msg_final[0])
            print(seq_list[int(msg_final[1])])
            response = seq_list[int(msg_final[1])]

        if msg_final[0] == "INFO":
            s = Seq(msg_final[1])
            count_bases = s.count()
            response += f"length {s.len()}"

            response = ""
            for base,value in count_bases.items():
                num_total = sum(count_bases.values())
                percentage = round((value / num_total) * 100, 2)
                print(f"{base} : {value} ({percentage})")
                response += f"{base} : {value} ({percentage})\n"

        if msg_final[0] == "COMP":
            print(msg_final[0])
            s = Seq(msg_final[1])
            complement = s.complement()
            response = complement
            print(response)

        if msg_final[0] == "REV":
            print(msg_final[0])
            s = Seq(msg_final[1])
            reverse = s.reverse()
            response = reverse
            print(response)

        if msg_final[0] == "GENE":
            print(msg_final[0])
            gene = msg_final[1]
            s = Seq()
            s.read_fasta(f"sequences/{gene}.txt")
            response = f"{s.strbases}\n"
            print(response)


        cs.send(response.encode())

        cs.close()