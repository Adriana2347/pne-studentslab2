from Seq0 import seq_read_fasta
from Seq0 import len_seq

content = input("enter a valid filename:")
filepath = input("enter a valid filename:")
filename = content + filepath
seq = seq_read_fasta(filename)
print(seq)