from pathlib import Path
import socket

class Client:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port


    def __str__(self):
        return self.ip, self.port

    def ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        message = "OK"
        s.send(str.encode(message))
        response = s.recv(2048)
        return response