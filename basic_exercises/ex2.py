text = "  Hello, World! Welcome to Python Programming.  "

stripped = text.strip()
print("Stripped", stripped)
new_text = text.split()
print("The number of words:", len(new_text))
print("All the words capitalized:", text.title())
print("The string starts with Hello?", stripped.startswith("Hello"))
print("The string ends with ing?", stripped.endswith("ing."))
print("The python position:", stripped.find("Python"))
joined = "-".join(new_text)
print("Joined", joined)