from pathlib import Path

FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()
body = file_contents.split("\n")
b = body[1:]
without_header = "\n".join(b)
print(without_header)

