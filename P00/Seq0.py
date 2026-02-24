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
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    result = ""
    for base in seq:
        result += complement[base]
    return result


def most_bases(count_dict):
    max_bases = max(count_dict, key=count_dict.get)
    return max_bases