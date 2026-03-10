from Seq1 import Seq
from client0 import Client

IP = "212.128.255.26"

PORT1 = 8080
PORT2 = 8081
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

folder = "sequences/"
filepath = "FRAT1.txt"
filename = folder + filepath

s = Seq()
s.read_fasta(filename)
sequence = str(s)
print("Gene FRAT1:", sequence + "...")

for i in range(10):
    fragment = sequence[i*10:(i+1)*10]
    print("Fragment", i+1, ":", fragment)
    if (i+1) % 2 != 0:
        c1.talk(fragment)
    else:
        c2.talk(fragment)