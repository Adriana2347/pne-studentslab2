class Seq:
    def __init__(self, strbases= None):
        if strbases is None:
            self.strbases = "NULL SEQUENCE!!"
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

    def __len__(self):
        return len(self.strbases)

    def count_bases(self, base):
        count = 0
        if self.strbases == "":
            return 0
        else:
            for b in self.strbases:
                if b in  base:
                    count += 1
            return count

