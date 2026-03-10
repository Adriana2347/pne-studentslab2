from Seq1 import Seq
from client0 import Client

IP = "212.128.255.104"
PORT = 8080
c = Client(IP, PORT)

genes = ["ADA", "U5", "FRAT1"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    s2 = Seq()
    s2.read_fasta(filename)
    print("To server:", "Sending", gene, "to server")
    c.talk(str(s2))
    print("From server:", c.talk(str(s2)))
    print("To server:", s2)
    print("From server:", c.talk(str(s2)))


