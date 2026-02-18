from Seq0 import seq_read_fasta
from Seq0 import seq_count

genes = ["ADA", "U5", "FRAT1", "FNX"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    seq = seq_read_fasta(filename)
    print(seq_count(seq))