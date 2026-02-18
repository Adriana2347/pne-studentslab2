from Seq0 import seq_read_fasta
from Seq0 import seq_count_bases

bases = ["A", "C", "G", "T"]

#Gene ADA

def exercise4(filename):
    bases = ["A", "C", "G", "T"]
    seq = seq_read_fasta(filename)
    for base in bases:
        total_count = seq_count_bases(seq, base)
    return base, total_count
filename = "sequences/ADA.txt"
print(exercise4(filename))

#Gene fNX
filename = "sequences/FNX.txt"
seq2 = seq_read_fasta(filename)
print("FNX:")
for base in bases:
    print(base, seq_count_bases(seq2, base))

#Gene U5
filename = "sequences/U5.txt"
seq3 = seq_read_fasta(filename)
print("U5:")
for base in bases:
    print(base, seq_count_bases(seq3, base))

#Gene FRAT1
filename = "sequences/FRAT1.txt"
seq4 = seq_read_fasta(filename)
print("FRAT1:")
for base in bases:
    print(base, seq_count_bases(seq4, base))