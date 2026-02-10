from dna_count import count_bases
from dna_count import total_len

with open("dna.txt", "r") as filename:
    content = filename.readlines()
    for line in content:
        seq = line.strip()
        print(count_bases(seq))
        print("The total lenght of the sequence is", total_len(seq))


with open("dna.txt", "r") as filename:
    content = filename.readlines()
    for line in content:
        lines = line.strip()
    print(lines)

#no hace falta volver a pegar la funcion, podemos poner from dna_count import_count bases

