from Seq1 import Seq

s1 = Seq()
s2 = Seq("TATAC")
s3 = Seq("AGCXTW")

print(f"Sequence: (Length: {len(s1)}) {s1} {s1.count_bases("A")}")
print(f"Sequence: (Length: {len(s2)}) {s2} {s2.count_bases("A")}")
print(f"Sequence: (Length: {len(s1)}) {s1} {s1.count_bases("A")}")

