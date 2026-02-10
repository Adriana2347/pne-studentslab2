
def total_len(sequence):
    return len(sequence)

def count_bases(sequence):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    i = 0
    while i < len(sequence):
        if sequence[i] == "A":
            count_a += 1
        elif sequence[i] == "C":
            count_c += 1
        elif sequence[i] == "G":
            count_g += 1
        elif sequence[i] == "T":
            count_t += 1
        i += 1
    return [count_a, count_c, count_t, count_g]

def main():
    seq = input("Enter a valid sequence: ").upper()
    N = count_bases(seq)
    total = total_len(seq)
    print("The total length is:", total)
    print("A", N[0])
    print("C", N[1])
    print("G", N[3])
    print("T", N[2])

if __name__ == "__main__":
    main()



