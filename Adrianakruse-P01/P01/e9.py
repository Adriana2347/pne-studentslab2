from Seq1 import Seq

# -- Create a Null sequence
s = Seq()

folder = "sequences/"
filepath = "U5.txt"
filename = folder + filepath

print(f"Sequence 1: {s.read_fasta(filename)}")
print(f"Sequence: (Length: {s.len()}) {s}")

print(f"Sequence:"
      f"A: {s.count_bases('A')} "
      f"C: {s.count_bases('C')} "
      f"T: {s.count_bases('T')} "
      f"G: {s.count_bases('G')}")

print(f"Reverse: {s.reverse()}")
print(f"Complement: {s.complement()}")


