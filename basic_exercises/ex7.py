student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("name:", student["name"])
subjects = student["subjects"]
print("Number of subjects:", len(subjects))


if "PNE" in student["subjects"]:
    print("True")
else:
    print("False")

for p in student["grades"]:
    if p == "Databases":
        print(p, student["grades"][p])

total = 0
persons = 0
for grade in student["grades"].values():
    total += grade
    persons += 1

mean = round(total / persons, 2)
print("The mean average is:", mean)

