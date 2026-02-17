from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")
b = body[1:]
without_header = "".join(b)
print("The number of bases is:", len(without_header))