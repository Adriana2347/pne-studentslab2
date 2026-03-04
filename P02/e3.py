from client0 import Client


IP = "212.128.255.104"
PORT = 8081
c = Client(IP, PORT)
# -- Send a message to the server
print(c)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
...
