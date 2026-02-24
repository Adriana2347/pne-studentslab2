
class Seq:
    def __init__(self, seq_list):
        self.seq_list = seq_list

    def __str__(self):
        """Method called when the object is being printed"""
        return self.seq_list

    def __len__(self):
        return len(self.seq_list)

def print_seqs(seq_list):
    index = 0
    for seq in seq_list:
        print(f"Sequence {index}: (Length: {len(seq)}) {seq}")
        index += 1


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)