from Seq0 import seq_read_fasta

folder = "sequences/"
filepath = "U5.txt"
filename = folder + filepath
function = seq_read_fasta(filename)

print(function[0:21])
