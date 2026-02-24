from Seq0 import seq_read_fasta
from Seq0 import seq_count
from Seq0 import most_bases


genes = ["ADA", "U5", "FRAT1", "FNX"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    seq = seq_read_fasta(filename)
    n = seq_count(seq)
    print("The most base", gene, "is:", most_bases(n))

