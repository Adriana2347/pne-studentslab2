from Seq1 import Seq


genes = ["ADA", "U5", "FRAT1", "FNX"]
for gene in genes:
    filename = "sequences/"+gene+".txt"
    s2 = Seq()
    s2.read_fasta(filename)
    print(f"Sequence: {gene}")
    count_dict = s2.count()
    print(f"Most frequent base: {s2.most_bases(count_dict)}")
