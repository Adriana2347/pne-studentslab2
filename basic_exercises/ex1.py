dna = "ATGCGATCGATCGATCGATCGA"

print("The total length of the string is:", len(dna))
print("First five characters:", dna[0:6])
print("Last three characters:", dna[-3:])
print("Dna in lowercase", dna.lower())

count = 0
i = 0
while i < len(dna):
    if dna[i: i + 3] == "ATC":
        i += 1
        count += 1
    else:
        i += 1
print("The number of dna ATC is:", count)
print("Replace dna:", dna.replace("T", "U"))