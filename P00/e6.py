from Seq0 import seq_read_fasta
from Seq0 import reverse

filename = "sequences/U5.txt"
seq = seq_read_fasta(filename)
n = 20
print(reverse(seq, n))