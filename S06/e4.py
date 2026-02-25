import termcolor

class Seq:
    def __init__(self, seq_list):
        self.seq_list = seq_list

    def __str__(self):
        """Method called when the object is being printed"""
        return self.seq_list

    def __len__(self):
        return len(self.seq_list)

def generate_seqs(pattern, number):
    new_list = []
    for seq in range(number):
        number_seq = pattern * (seq + 1)
        new_list.append(Seq(number_seq))
    return new_list

def print_seqs(seq_list):
    index = 0
    for seq in seq_list:
        print(f"Sequence {index}: (Length: {len(seq)}) {seq}")
        index += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
termcolor.cprint(seq_list1, color=green)

print()
print("List 2:")
print_seqs(seq_list2)
