from echo-server3

while count < 5:
    c = Client(IP, PORT)
    c.talk(str(msg))
    print("Message recived:", count)