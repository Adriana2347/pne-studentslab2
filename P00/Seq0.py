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
    print(len(seq))
