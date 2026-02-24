from Seq0 import seq_read_fasta
from Seq0 import seq_complement

filename = "sequences/U5.txt"
seq = seq_read_fasta(filename)
new_seq = seq[0:21]
complement = seq_complement(new_seq)
print(new_seq)
print(complement)