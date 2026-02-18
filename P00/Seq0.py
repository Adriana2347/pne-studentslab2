from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    body = file_contents.split("\n")
    b = body[1:]
    without_header = "".join(b)
    return without_header

def len_seq(seq):
    return len(seq)

def seq_count_bases(seq, bases):
    count = 0
    for base in seq:
        if base == bases:
            count += 1
    return count

def seq_count(seq):
    count_dict = {}
    i = 0
    for base in seq:
        if base not in count_dict:
            count_dict[base] = 1
        else:
            count_dict[base] += 1
        i += 1
    return count_dict

def reverse(seq, n):
    new_seq = seq[:n]
    reverse = new_seq[::-1]
    return reverse

def seq_complement(seq):
    i = 0
    for base in seq:
        if base == "A":
            result = seq.replace("T")
        elif base == "C":
            result = seq.replace("G")
        i += 1
    return