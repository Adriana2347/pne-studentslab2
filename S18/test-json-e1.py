import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)


for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person["Firstname"], person["Lastname"])
    termcolor.cprint("Age: ", 'green', end="")
    print(person["age"])
    phone_numbers = person["phoneNumber"]
    termcolor.cprint("Phone numbers: ", 'green', end="")
    print(len(phone_numbers))


    for i, mobile in enumerate(phone_numbers):
        termcolor.cprint(f"  Phone {i}:", 'blue')
        termcolor.cprint("    Type: ", 'red', end="")
        print(mobile["type"])
        termcolor.cprint("    Number: ", 'red', end="")
        print(mobile["number"])
