from pathlib import Path

FILENAME = "sequences/RNU6.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
# -- Print the contents on the console
print(file_contents)
