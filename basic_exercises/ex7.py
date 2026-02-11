student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("name:", student["name"])
subjects = student["subjects"]
print("Number of subjects:", len(subjects))

for p in subjects:
    if p == "PNE":
        print("True")

