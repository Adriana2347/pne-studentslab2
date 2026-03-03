from Seq1 import Seq

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("AGCXTW")


print(f"Sequence: (Length: {s1.len()}) {s1} "
      f"A: {s1.count_bases('A')} "
      f"C: {s1.count_bases('C')} "
      f"T: {s1.count_bases('T')} "
      f"G: {s1.count_bases('G')}")
print(f"Sequence: (Length: {s2.len()}) {s2} "
      f"A: {s2.count_bases('A')} "
      f"C: {s2.count_bases('C')} "
      f"T: {s2.count_bases('T')} "
      f"G: {s2.count_bases('G')}")
print(f"Sequence: (Length: {s3.len()}) {s3} "
      f"A: {s3.count_bases('A')} "
      f"C: {s3.count_bases('C')} "
      f"T: {s3.count_bases('T')} "
      f"G: {s3.count_bases('G')}")