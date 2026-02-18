from Seq0 import seq_read_fasta
from Seq0 import len_seq


list_gene = ["ADA", "U5", "FRAT1", "FNX"]
for genes in list_gene:
    folder = "sequences/"
    gene = genes + ".txt"
    filename = folder + gene
    seq = seq_read_fasta(filename)
    length = len_seq(seq)
    print(gene, ":", length)

