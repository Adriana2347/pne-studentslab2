class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        valid = ["A", "C", "G", "T"]
        for base in strbases:
            if base not in valid:
                self.strbases = "ERROR!!"
                print("Error!!")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print("Testing....")
