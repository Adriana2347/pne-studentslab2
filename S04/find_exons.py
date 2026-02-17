from pathlib import Path

FILENAME = "sequences/ADA_exons.txt"

file_contents = Path(FILENAME).read_text()
body = file_contents.split("\n")
b = "".join(body)
first_exon = b.find("GCTGGCCCCAGGGAAAGCCGAGCGGCCACCGAGCCGGCAGAGACCCACCGAGCGGCGGCGGAGGGAGCAGCGCCGGGGCGCACGAGGGCACCATGGCCCAGACGCCCGCCTTCGACAAGCCCAAA")


FILENAME2 = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
body2 = file_contents.split("\n")
b2 = "".join(body2)
first_exon = b2.find("GCTGGCCCCAGGGAAAGCCGAGCGGCCACCGAGCCGGCAGAGACCCACCGAGCGGCGGCGGAGGGAGCAGCGCCGGGGCGCACGAGGGCACCATGGCCCAGACGCCCGCCTTCGACAAGCCCAAA")
print(first_exon)