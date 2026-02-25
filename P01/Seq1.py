from pathlib import Path

class Seq:
    def __init__(self, strbases= None):
        if strbases is None:
            self.strbases = "NULL"
            print("Null sequence...")
        else:
            valid = ["A", "C", "G", "T"]
            for base in strbases:
                if base not in valid:
                    self.strbases = "INVALID SEQUENCE!"
                    print("Invalid sequence...")
                    return
            self.strbases = strbases
            print("New sequence created!")


    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "INVALID SEQUENCE!":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_bases(self, base):
        count = 0
        if self.strbases == "NULL" or self.strbases == "INVALID SEQUENCE!" :
            return 0
        else:
            for b in self.strbases:
                if b in  base:
                    count += 1
            return count

    def count(self):
        count_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "NULL" or self.strbases == "INVALID SEQUENCE!":
            return count_dict
        else:
            for b in self.strbases:
                if b not in count_dict:
                    count_dict[b] = 1
                else:
                    count_dict[b] += 1
        return count_dict

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "INVALID SEQUENCE!":
            result = "ERROR!"
        else:
            result = self.strbases[::-1]
        return result

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "INVALID SEQUENCE!":
            result = "ERROR!"
        else:
            complement = {
                "A": "U",
                "T": "A",
                "C": "G",
                "G": "C"

            }
            result = ""
            for base in self.strbases:
                result += complement[base]
        return result

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        body = file_contents.split("\n")
        b = body[1:]
        without_header = "".join(b)
        self.strbases = without_header

    def most_bases(self, count_dict):
        max_bases = max(count_dict, key=count_dict.get)
        return max_bases









