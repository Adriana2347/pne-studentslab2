from Seq1 import Seq
from client0 import Client

IP = "212.128.255.104"
PORT = 8080
c = Client(IP, PORT)

folder = "sequences/"
filepath = "FRAT1.txt"
filename = folder + filepath
s2 = Seq()
s2.read_fasta(filename)
sequence = str(s2)

start = 0
for i in range(5):
    fragment = sequence[start:start+10]
    print("Fragment", i+1, ":", fragment)
    c.talk(fragment)
    start += 10
