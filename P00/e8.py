from Seq0 import seq_read_fasta
from Seq0 import seq_count
from Seq0 import most_bases

filename = "sequences/U5.txt"
seq = seq_read_fasta(filename)

n = seq_count(seq)
print(most_bases(n))
