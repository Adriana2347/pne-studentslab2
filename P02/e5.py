from Seq1 import Seq
from client0 import Client

IP = "212.128.255.104"
PORT = 8081
c = Client(IP, PORT)

folder = "sequences/"
filepath = "FRAT1.txt"
filename = folder + filepath
s2 = Seq()
s2.read_fasta(filename)
sequence = str(s2)

i = 0
start = 0
for i in range(0, 6):
    sequence_1 = sequence[start:start+10]
    c.talk(str(sequence))
    i += 1
    start += 10
