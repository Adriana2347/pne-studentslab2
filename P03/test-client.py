from client0 import Client
import socket

if __name__ == "__main__":

    IP = "127.0.0.1"
    PORT = 8080

    print("-------PRACTICE-------")
    print(f"connection to SERVER at {IP}, PORT: {PORT}")

    c = Client(IP, PORT)

    print("Testing Ping...")
    response = c.talk("PING")
    print(response)
    print()

    print("Testing Get...")
    sequences = []
    for i in range(5):
        response = c.talk(f"GET {i}")
        sequences.append(response)
        print(f"Get {i}: {response}")
    print()

    seq0 = sequences[0]

    print("Testing info...")
    response = c.talk(f"INFO {seq0}")
    print(response)
    print()

    print("Testing COMP...")
    response = c.talk(f"COMP {seq0}")
    print(response)
    print()

    print("Testing REV...")
    response = c.talk(f"REV {seq0}")
    print(response)
    print()

    print("Testing GENE...")
    genes = ["U5", "ADA", "FRAT1", "FXN"]


